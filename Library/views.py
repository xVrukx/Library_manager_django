# views.py
from django.shortcuts import render, redirect
from .models import Book, Member, borrow
from log_and_re.models import register
from django.contrib import messages

# View to display library page
def Library(request):


    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        number = request.POST.get('number')


        try:
            user = register.objects.get(username=username)
            user.email = email
            user.password = password
            user.number = number
            user.save()
            request.session['username'] = username
            request.session['email'] = email
            request.session['password'] = password
            request.session['number'] = number
        except register.DoesNotExist as e:
            print(f"Error: {e}")
            messages.error(request, "User does not exist.")

    username = request.session.get('username', 'Guest')
    email = request.session.get('email', 'Guest@gmail.com')
    password = request.session.get('password', 'Guest')
    number = request.session.get('number', 'Guest')

    books = Book.objects.all()
    members = Member.objects.all()
    borrowed = borrow.objects.all()
    context = {
        'username': username,
        'email': email,
        'password': password,
        'number': number,
        'books': books,
        'members': members,
        "borrowed": borrowed
    }
    return render(request, 'app.html', context)

# View to add a new book
def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        quantity = request.POST['quantity']

        Book.objects.create(title=title, author=author, quantity=quantity)
        messages.success(request, 'Book added successfully!')
    return redirect('Library')

# View to add a new member
def add_member(request):
    if request.method == 'POST':
        name = request.POST['name']
        Member.objects.create(name=name)
        messages.success(request, 'Member added successfully!')
    return redirect('Library')

# View to handle borrowing or returning a book
def borrow_and_return(request):
    if request.method == 'POST':
        action = request.POST.get('action')  # either 'borrow' or 'return'
        member_id = request.POST.get('member_id')
        book_id = request.POST.get('book_id')

        try:
            member = Member.objects.get(id=member_id)
            book = Book.objects.get(id=book_id)
        except (Member.DoesNotExist, Book.DoesNotExist):
            messages.error(request, "Invalid Member or Book ID")
            return redirect('Library')

        if action == 'borrow':
            if book.quantity <= 0:
                messages.warning(request, f"No copies of {book.title} are available.")
            else:
                borrow.objects.create(Name=member, Books=book)
                book.quantity -= 1
                book.save()
                messages.success(request, f"{book.title} borrowed by {member.name}.")

        elif action == 'return':
            try:
                borrowed_entry = borrow.objects.filter(Name=member, Books=book)
                count = borrowed_entry.count()
                borrowed_entry.delete()
                book.quantity += count
                book.save()
                messages.success(request, f"{book.title} returned by {member.name}.")
            except borrow.DoesNotExist:
                messages.warning(request, "This borrow record does not exist.")

    return redirect('Library')
