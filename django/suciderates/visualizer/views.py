import base64
import io
from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import matplotlib

matplotlib.use('Agg')
# Read in the suicide dataset
df = pd.read_csv('SuicideChina.csv')
df['Died'] = df['Died'].map({'no': 0, 'yes': 1})
# Create your views here.
@csrf_exempt
def gender_suicide(request):
    # Generate the bar plot of suicide rates by gender
    plt.clf()
    sns.countplot(x='Sex', data=df,hue= 'Died')
    plt.xlabel('Gender')
    plt.ylabel('Number of Deaths')
    plt.title('Suicide Rates by Gender')

    # Render the plot to a PNG image and convert to bytes
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_data = buffer.getvalue()

    # Pass the image data to the template
    context = {'image_data': base64.b64encode(image_data).decode('utf-8')}

    # Render the template
    return render(request, 'gender.html', context)

@csrf_exempt
def age_suicide(request):
    plt.clf()
    sns.histplot(df['Age'], kde=False, bins=20)
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.title('Distribution of Ages in Suicide Dataset')

    # Render the plot to a PNG image and convert to bytes
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_data = buffer.getvalue()

    # Pass the image data to the template
    context = {'image_data': base64.b64encode(image_data).decode('utf-8')}

    # Render the template
    return render(request, 'age.html', context)

@csrf_exempt
def education_suicide(request):
    plt.clf()
    sns.scatterplot(x='Age', y='Education', data=df)
    plt.xlabel('Age')
    plt.ylabel('Education Level')
    plt.title('Age versus Education Level')

    # Render the plot to a PNG image and convert to bytes
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_data = buffer.getvalue()

    # Pass the image data to the template
    context = {'image_data': base64.b64encode(image_data).decode('utf-8')}

    # Render the template
    return render(request, 'education.html', context)

@csrf_exempt
def occupation_suicide(request):
    plt.clf()
    sns.boxplot(x='Occupation', y='Died', data=df)
    plt.xlabel('Occupation')
    plt.ylabel('Number of Deaths')
    plt.title('Suicide Rates by Occupation')
    plt.xticks(rotation=90)

    # Render the plot to a PNG image and convert to bytes
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_data = buffer.getvalue()

    # Pass the image data to the template
    context = {'image_data': base64.b64encode(image_data).decode('utf-8')}

    # Render the template
    return render(request, 'occupation.html', context)

@csrf_exempt
def suicide_time(request):
    plt.clf()
    suicide_rates = df.groupby('Year')['Died'].sum().reset_index()
    sns.lineplot(x='Year', y='Died', data=suicide_rates)
    plt.xlabel('Year')
    plt.ylabel('Number of Deaths')
    plt.title('Suicide Rates Over Time')
    plt.xticks(rotation=90)

    # Render the plot to a PNG image and convert to bytes
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_data = buffer.getvalue()

    # Pass the image data to the template
    context = {'image_data': base64.b64encode(image_data).decode('utf-8')}

    # Render the template
    return render(request, 'time.html', context)
