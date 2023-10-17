import re
from django import forms
from .models import ContactUs, Member


class AddMemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ["first_name", "last_name", "phone"]

    # this function will be used for the validation
    def clean(self):
        # data from the form is fetched using super function
        super(AddMemberForm, self).clean()

        # extract the first_name and text field from the data
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        phone = self.cleaned_data.get("phone")
        print(phone)

        # conditions to be met for the first_name length
        if first_name is not None and len(first_name) < 3:
            self._errors["first_name"] = self.error_class(
                ["Minimum 3 characters required"]
            )
        if last_name is not None and len(last_name) < 3:
            self._errors["last_name"] = self.error_class(
                ["Minimum 3 characters required"]
            )
        if phone is not None and len(str(phone)) != 10 or len(str(phone)) > 10:
            self._errors["phone"] = self.error_class(
                ["Phone Number Should Contain a exact of 10 Numbers"]
            )

        # return any errors if found
        return self.cleaned_data


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ["name", "email", "message"]

    def clean(self):
        super(ContactUsForm, self).clean()

        email = self.cleaned_data.get("email")

        valid_email_format = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
        if not re.match(valid_email_format, email):
            self._errors["email"] = self.error_class(["Invalid Email"])

        return self.cleaned_data
