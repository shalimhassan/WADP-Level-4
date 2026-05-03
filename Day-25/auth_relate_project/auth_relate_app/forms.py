from django import form


class ProfileForm(forms.ModelForm):
  class Meta:
    exclude=['user']
    widgets={
      'dob':forms.DateInput(attrs={
        'type':'date'
      })
    }
    
class ProductForm(forms.ModelForm):
  class Meta:
    model = ProductModel
    fiels = '__all__'
    exclude = ['total_amount', 'created_by']
    