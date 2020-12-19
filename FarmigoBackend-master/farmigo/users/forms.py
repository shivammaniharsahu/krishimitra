from crispy_forms.helper import FormHelper
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import BaseUser, Farmer, Retailer, Supplier
from .models import Crop, FarmerProduct, Livestock, RetailerProduct, SupplierProduct

#BaseUser
class BaseUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = BaseUser
        form_show_labels = False
        fields = ['user_type', 'name', 'email', 'mobnumber', 'state', 'district', 'address']
    def __init__(self, *args, **kwargs):
        super(BaseUserCreationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False 
        
class BaseUserUpdateForm(forms.ModelForm):
    class Meta(forms.ModelForm):
        model = BaseUser
        form_show_labels = False

        fields = ['user_type', 'name', 'email', 'mobnumber', 'state', 'district', 'address']
    def __init__(self, *args, **kwargs):
        super(BaseUserUpdateForm, self).__init__(*args, **kwargs)
        # self.helper = FormHelper()
        # self.helper.form_show_labels = False 

#Farmer
class FarmerCreationForm(forms.ModelForm):
    class Meta(forms.ModelForm):
        model = Farmer
        fields = ['op_land_area', 'dob']
class FarmerUpdateForm(forms.ModelForm):
    class Meta(forms.ModelForm):
        model = Farmer
        fields = ['op_land_area', 'dob']

class CropCreationForm(forms.ModelForm):
    class Meta(forms.ModelForm):
        model = Crop
        fields = ['crop_name', 'crop_type']
class CropUpdateForm(forms.ModelForm):
    class Meta(forms.ModelForm):
        model = Crop
        fields = ['crop_name', 'crop_type']

class FarmerProductCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = FarmerProduct
        fields = ['farmer', 'product_name', 'quality_index', 'product_type']
class FarmerProductChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = FarmerProduct
        fields = ['product_name', 'quality_index', 'product_type']

#Retailer
class RetailerUpdateForm(forms.ModelForm):
    class Meta(forms.ModelForm):
        model = Retailer
        fields = ['description']




