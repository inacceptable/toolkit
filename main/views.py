from django.shortcuts import render
import requests 
from django.http import JsonResponse
import string
from django.core.files.storage import default_storage
from random import * 
from django.conf import settings
import textwrap
import os 
from docx2pdf import convert
import re 
from fpdf import FPDF
from .models import txt_to_pdf, feedback, docx_to_pdf

def home(request):
	tool_list = [['Decimal to binary', 'html/decimal_to_binary.html'], ['Binary to Decimal', 'html/binary_to_decimal.html'], ['Password Generator','html/password_generator.html'], ['Hours to seconds converter', 'html/hours_to_seconds_converter.html'], ['Hours to minutes', 'html/hours_to_minutes.html'], ['TXT document to pdf', 'html/txt_document_to_pdf.html'], ['DOCX to PDF', 'html/docx_to_pdf.html']]
	context = {
		'tool_list' : tool_list, 

	} 
	return render(request, 'html/home.html', context)

def binary_to_number_converter(request):
	number_input = str(request.GET.get('inputted'))
	if "0b" in number_input:
		number_input = number_input.replace("Ob","")
	try:	
		new_number = int(number_input, 2)
	except: 
		new_number = "Please enter a valid number."
	new_number = str(new_number)

	data = {
		'new_number' : new_number, 
	}
	return JsonResponse(data) 

def number_to_binary_converter(request):
	new_number = str(request.GET.get('inputted'))
	new_number = bin(int(new_number))
	data = { 
		'new_number' : new_number,
	}
	return JsonResponse(data) 

def password_generator(reqeust): 
	characters = string.ascii_letters + string.punctuation + string.digits 
	new_number = "".join(choice(characters) for x in range(randint(8,16)))
	data = {
		'new_number' : new_number, 
	}
	return JsonResponse(data)

def hours_to_seconds(request):
	new_number = str(request.GET.get('inputted'))
	try:
		new_number = float(new_number) * 60 * 60
	except: 
		new_number = "Please enter a valid number."
	data = {
		'new_number' : new_number,
	}
	return JsonResponse(data)

def hours_to_minutes(request):
	new_number = str(request.GET.get('inputted'))
	try:
		new_number = float(new_number) * 60 
	except: 
		new_number = "Please enter a valid number."
	data = {
		'new_number' : new_number,
	}
	return JsonResponse(data)
def txt_document_to_pdf(request): 
	txt_file = request.FILES.get('txt_file')
	new_object = txt_to_pdf(txt_file = request.FILES.get('txt_file'))
	pdf = FPDF() 
	pdf.add_page() 
	pdf.set_font('arial', size=10)
	path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
	new_object.save()
	txt_path = path+new_object.txt_file.url
	pdf_c_path = txt_path.replace(".txt", ".pdf")
	pdf_path = "http://127.0.0.1:8000" + new_object.txt_file.url
	pdf_path = pdf_path.replace(".txt", ".pdf")
	text_file = open(txt_path, 'r')
	for text in text_file:
		pdf.cell(200, 10, txt = text, ln=1,align='L') 
	pdf.output(pdf_c_path)	
	new_object.pdf_file = pdf_path
	new_object.save()
	data = {
		'pdf_path' : pdf_path
		}
	return JsonResponse(data)
