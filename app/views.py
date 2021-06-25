from django.shortcuts import render, redirect
from django.views import View
from .models import Interviews, Users, UserInterviews
from datetime import datetime
from django.core.mail import send_mail
# function to find users


def findUsers(data):
    user_id = []
    for i in data.keys():
        if i.startswith('user-'):
            g, Id = i.split('-')
            user_id += [int(Id)]
    return user_id


def filterDate(d):
    date, time = d.split('T')
    year, month, day = date.split('-')
    hr, min = time.split(':')
    d = datetime(int(year), int(
        month), int(day), int(hr), int(min), 0)
    return d


def rawtime(d):
    year, month, day = str(d.year), str(d.month), str(d.day)
    hr, min = str(d.hour), str(d.minute)
    date_time = [year, month, day, hr, min]
    for i in range(5):
        if len(date_time[i]) == 1:
            date_time[i] = '0' + date_time[i]
    date_t = date_time[0] + '-' + date_time[1] + '-' + \
        date_time[2] + 'T' + date_time[3] + ':' + date_time[4]
    return date_t


def compare(st, ed, start, end):
    now = datetime(2021, 1, 1, 0, 0, 0)
    st = datetime(st.year, st.month, st.day, st.hour, st.minute, st.second)
    ed = datetime(end.year, end.month, end.day,
                  end.hour, end.minute, end.second)
    intervals = [0]*4
    intervals[0] = divmod((st - now).total_seconds(), 3600)[0]
    intervals[1] = divmod((ed - now).total_seconds(), 3600)[0]
    intervals[2] = divmod((start - now).total_seconds(), 3600)[0]
    intervals[3] = divmod((end - now).total_seconds(), 3600)[0]

    if not((intervals[1] < intervals[2]) or (intervals[3] < intervals[0])):
        return True
    return False


class DashboardView(View):
    def get(self, request):
        users = Users.objects.all()
        return render(request, 'app/dashboard.html', {'users': users})

    def post(self, request):
        allusers = Users.objects.all()
        data = request.POST
        # taking out users
        user_id = findUsers(data)
        start = filterDate(data['start-time'])
        end = filterDate(data['end-time'])

        if len(user_id) < 2:
            return render(request, 'app/dashboard.html', {'users': allusers, 'error': "Interview should have atleast two users!!"})

        # checking for clashes of interviews
        for ID in user_id:
            user = Users.objects.get(id=ID)
            user_interviews = UserInterviews.objects.filter(user=user)
            for obj in user_interviews:
                interviews = obj.interview
                st = interviews.startTime
                ed = interviews.endTime
                if compare(st, ed, start, end):
                    return render(request, 'app/dashboard.html', {'users': allusers, 'error': str(user.name) + " has already scheduled an interview at given time."})

        # creating Interview

        interview = Interviews(startTime=start, endTime=end)
        interview.save()

        for ID in user_id:
            user = Users.objects.get(id=ID)
            UserInterviews(user=user, interview=interview).save()

            subject = "My mail"
            message = "You have an interview"
            email = user.email
            send_mail(
                subject,
                message,
                email,
                ['1805213002@ietlucknow.ac.in'],
                fail_silently=False,
            )

        return render(request, 'app/dashboard.html', {'users': allusers, 'success': "Your interview is created successfully!!"})


class InterviewsClass(View):
    def get(self, request):
        all_interviews = Interviews.objects.all()
        context = []
        for interview in all_interviews:
            interview_users = UserInterviews.objects.filter(
                interview=interview)
            if interview_users:
                details = [interview_users] + [interview]
                context.append(details)
        print(context)
        return render(request, 'app/interviews.html', {'datas': context})


def update(request):
    all_interviews = Interviews.objects.all()
    context = []
    for interview in all_interviews:
        interview_users = UserInterviews.objects.filter(
            interview=interview)
        if interview_users:
            details = [interview_users] + [interview]
            context.append(details)
    # print(context)
    return render(request, 'app/update.html', {'datas': context})


def update_data(request, id):
    interview = Interviews.objects.get(pk=id)
    user_interviews = UserInterviews.objects.filter(interview=interview)
    selected_users = []
    for usr in user_interviews:
        selected_users += [usr.user]
    start = interview.startTime
    end = interview.endTime
    users = Users.objects.all()
    not_selectedusers = []
    for usr in users:
        if usr not in selected_users:
            not_selectedusers += [usr]
    start_time = rawtime(start)
    end_time = rawtime(end)
    if request.method == 'GET':
        return render(request, 'app/update_interview.html', {'selected_users': selected_users, 'not_selectedusers': not_selectedusers, 'id': id, 'start_time': start_time, 'end_time': end_time})
    else:
        id = request.POST['Id']
        interview_to_update = Interviews.objects.get(pk=id)
        allusers = Users.objects.all()
        data = request.POST
        # taking out users
        user_id = findUsers(data)
        start = filterDate(data['start-time'])
        end = filterDate(data['end-time'])

        if len(user_id) < 2:
            return render(request, 'app/update_interview.html', {'selected_users': selected_users, 'not_selectedusers': not_selectedusers, 'id': id, 'start_time': start_time, 'end_time': end_time, 'error': "Interview should have atleast two users!!"})

        # checking for clashes of interviews
        for ID in user_id:
            user = Users.objects.get(id=ID)
            user_interviews = UserInterviews.objects.filter(user=user)
            for obj in user_interviews:
                interviews = obj.interview
                if interviews != interview_to_update:
                    st = interviews.startTime
                    if compare(st, end):
                        return render(request, 'app/update_interview.html', {'selected_users': selected_users, 'not_selectedusers': not_selectedusers, 'id': id, 'start_time': start_time, 'end_time': end_time, 'error': str(user.name) + " has already scheduled an interview at given time."})

        # creating Interview
        interview_to_update.delete()
        interview = Interviews(startTime=start, endTime=end)
        interview.save()

        for ID in user_id:
            user = Users.objects.get(id=ID)
            UserInterviews(user=user, interview=interview).save()

        return render(request, 'app/dashboard.html', {'users': allusers, 'success': "Your interview is created successfully!!"})
