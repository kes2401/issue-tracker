from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.db.models.functions import Lower
from django.db.models import Count
from .forms import CreateIssue
from .models import Issue, IssueComment, IssueVote
from cart.forms import Cart_New_feature
from cart.models import Cart
from django.http import HttpResponse


def tracker(request):
    """ Renders the Tracker page that tracks and manages all bug reports and feature requests """
    bugs = Issue.objects.filter(issue_type='bug')
    features = Issue.objects.filter(issue_type='feature')

    if request.method == 'POST':
        if request.POST.get('bug-search') != None:
            bug_search_term = request.POST.get('bug-search')
            bugs = bugs.filter(title__icontains=bug_search_term)
        elif request.POST.get('feature-search') != None:
            feature_search_term = request.POST.get('feature-search')
            features = features.filter(title__icontains=feature_search_term)
        
        if request.POST.get('bugStatus') == 'pending':
            bugs = bugs.filter(status='pending')
        elif request.POST.get('bugStatus') == 'in-progress':
            bugs = bugs.filter(status='in progress')
        elif request.POST.get('bugStatus') == 'closed':
            bugs = bugs.filter(status='closed')

        if request.POST.get('featureStatus') == 'pending':
            features = features.filter(status='pending')
        elif request.POST.get('featureStatus') == 'in-progress':
            features = features.filter(status='in progress')
        elif request.POST.get('featureStatus') == 'closed':
            features = features.filter(status='closed')
        
        if request.POST.get('bugSort') == 'name-down':
            bugs = bugs.order_by(Lower('title').asc())
        elif request.POST.get('bugSort') == 'name-up':
            bugs = bugs.order_by(Lower('title').desc())
        elif request.POST.get('bugSort') == 'votes-down':
            bugs = bugs.annotate(num_votes=Count('issuevote')).order_by('-num_votes')
        elif request.POST.get('bugSort') == 'votes-up':
            bugs = bugs.annotate(num_votes=Count('issuevote')).order_by('num_votes')
        elif request.POST.get('bugSort') == 'comments-down':
            bugs = bugs.annotate(num_comments=Count('issuecomment')).order_by('-num_comments')
        elif request.POST.get('bugSort') == 'comments-up':
            bugs = bugs.annotate(num_comments=Count('issuecomment')).order_by('num_comments')
        
        if request.POST.get('featureSort') == 'name-down':
            features = features.order_by(Lower('title').asc())
        elif request.POST.get('featureSort') == 'name-up':
            features = features.order_by(Lower('title').desc())
        elif request.POST.get('featureSort') == 'votes-down':
            features = features.annotate(num_votes=Count('issuevote')).order_by('-num_votes')
        elif request.POST.get('featureSort') == 'votes-up':
            features = features.annotate(num_votes=Count('issuevote')).order_by('num_votes')
        elif request.POST.get('featureSort') == 'comments-down':
            features = features.annotate(num_comments=Count('issuecomment')).order_by('-num_comments')
        elif request.POST.get('featureSort') == 'comments-up':
            features = features.annotate(num_comments=Count('issuecomment')).order_by('num_comments')

    comments = IssueComment.objects.all()
    votes = IssueVote.objects.all()
    for bug in bugs:
        bug.comments = comments.filter(issue=bug.pk).count()
        bug.votes = votes.filter(issue=bug.pk).count()
    for feature in features:
        feature.comments = comments.filter(issue=feature.pk).count()
        feature.votes = votes.filter(issue=feature.pk).count()

    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(user=request.user).count()
    else:
        cart_count = 0 

    return render(request, 'tracker.html', {
        'bugs': bugs,
        'features': features,
        'cart_count': cart_count
    })


@login_required
def create_bug(request):
    """ Render page providing form to user to report a new bug """
    if request.method == 'POST':
        form = CreateIssue(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.issue_type = 'bug'
            instance.author = request.user
            instance.save()
            messages.success(
                request, 'You have successfully reported a new bug.')
        else:
            messages.error(
                request, 'Something went wrong. Please try again.')
        return redirect('tracker')
    else:
        form = CreateIssue()
        cart_count = Cart.objects.filter(user=request.user).count()
    return render(request, 'create_bug.html', {
        'form': form,
        'cart_count': cart_count
    })


@login_required
def create_feature(request):
    """ Render page providing form to user to create a new feature request for their cart """
    form = Cart_New_feature()
    cart_count = Cart.objects.filter(user=request.user).count()    
    return render(request, 'create_feature.html', {
        'form': form,
        'cart_count': cart_count
    })


@ensure_csrf_cookie
def bug_detail(request, id):
    bug = Issue.objects.get(pk=id)
    comments = IssueComment.objects.all().filter(issue=id).order_by('date_published')
    votes = IssueVote.objects.all().filter(issue=id)
    votes_count = votes.count()
    for vote in votes:
        if vote.user == request.user:
            user_vote = True
            break
    else:
        user_vote = False

    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(user=request.user).count()
    else:
        cart_count = 0 

    return render(request, 'issue_detail.html', {
        'issue': bug,
        'comments': comments,
        'votes_count': votes_count,
        'user_vote': user_vote,
        'cart_count': cart_count
    })


@ensure_csrf_cookie
def feature_detail(request, id):
    feature = Issue.objects.get(pk=id)
    comments = IssueComment.objects.all().filter(issue=id).order_by('date_published')
    votes = IssueVote.objects.all().filter(issue=id)
    votes_count = votes.count()
    for vote in votes:
        if vote.user == request.user:
            user_vote = True
            break
    else:
        user_vote = False
    
    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(user=request.user).count()
    else:
        cart_count = 0 

    return render(request, 'issue_detail.html', {
        'issue': feature,
        'comments': comments,
        'votes_count': votes_count,
        'user_vote': user_vote,
        'cart_count': cart_count
    })


def add_comment(request, id):
    if request.method == 'POST':
        new_comment = IssueComment(comment=request.POST.get('comment'))
        current_user = User.objects.get(username=request.user)
        current_issue = Issue.objects.get(pk=id)
        new_comment.user = current_user
        new_comment.issue = current_issue
        new_comment.save()
        savetime = IssueComment.objects.get(
            user=request.user, comment=request.POST.get('comment'), issue=current_issue.pk)
        return HttpResponse(savetime.date_published)


def add_vote(request, id):
    if request.method == 'POST':
        new_vote = IssueVote()
        current_user = User.objects.get(username=request.user)
        current_issue = Issue.objects.get(pk=id)
        new_vote.issue = current_issue
        new_vote.user = current_user
        new_vote.save()
        return HttpResponse('added')


def remove_vote(request, id):
    if request.method == 'POST':
        current_user = User.objects.get(username=request.user)
        current_issue = Issue.objects.get(pk=id)
        IssueVote.objects.get(user=current_user, issue=current_issue).delete()
        return HttpResponse('removed')
