from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import ContactForm

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})

def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contacts/contact_detail.html', {'contact': contact})

def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'contacts/contact_form.html', {'form': form})
def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)

    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list') 

    return render(request, 'contacts/contact_detail.html', {'contact': contact})
def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)  # Get the contact object by its primary key (pk).
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()  # Save the updated contact.
            return redirect('contact_list')  # Redirect to the contact list page.
    else:
        form = ContactForm(instance=contact)  # Populate the form with the current contact details.
    return render(request, 'contacts/edit_contact.html', {'form': form})
def landing_page(request):
    return render(request, 'landing_page.html')

