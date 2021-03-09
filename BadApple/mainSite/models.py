# General imports:
from django.db import models
from uuid import uuid4

# Import reference data:
from mainSite.extendedModels.modelCodes import *

# Import administrative models:
from mainSite.extendedModels.administrative import *



# Main database models:

class PRATemplate(models.Model):
	# Choices:
	SUBJECTS = [
					('0' , 'Body Worn Cameras'),
					('1' , 'Unmanned Aerial Vehicles (Drones)'),
					('2' , 'Facial Recognition'),
					('3' , 'Thermographic Cameras (FLIR)'),
					('4' , 'License Plate Readers'),
					('5' , 'Federal MOUs (Memoranda of Understanding)'),
					('6' , 'Predictive Policing'),
					('7' , 'Gunshot Detection Microphones (ShotSpotter)'),
					('8' , 'Social Media Monitoring'),
					('9' , 'IMSI-Catcher Equipment (Stingray)'),
					('10' , 'Police Misconduct - Based on the Officer\'s Name'),
					('11' , 'Police Misconduct - Based on the Incident')
				]

	# Filters:
	country = models.CharField('Country' , max_length = 3 , choices = COUNTRIES , default = 'USA')
	stateTerritoryProvince = models.CharField('State/Territory/Province' , max_length = 6 , choices = STATES_TERRITORIES_PROVINCES , default = 'USA-CA')
	subject = models.CharField('Subject' , max_length = 4 , choices = SUBJECTS , default = '0')

	# Template Contents:
	title = models.CharField('Title' , max_length = 300 , blank = True)
	letterBody = models.TextField('Letter Body' , max_length = 10000 , blank = True)

	# Administrative:
	createdOn = models.DateTimeField('Template Created On (Auto-Filled)' , auto_now_add = True)
	updatedOn = models.DateTimeField('Template Last Updated On (Auto-Filled)' , auto_now = True)
	lastChangedBy = models.CharField('Last Changed By' , max_length = 50 , blank = True)
	toBeDeleted = models.BooleanField('Delete' , default = False)
	daysUntilDeletion = models.IntegerField('Days Until Deletion (When Marked For Deletion)' , default = 30)

	# Permissions:
	approved = models.BooleanField('Template Approved' , default = False)
	public = models.BooleanField('Template Public' , default = False)



	# Manage metadata:
	class Meta:
		verbose_name = 'PRA Template'
		verbose_name_plural = 'PRA Templates'



class OversightCommission(models.Model):
	def generateUniqueID():
		while (True):
			uniqueID = str(uuid4())
			if (len(OversightCommission.objects.filter(commissionID = uniqueID)) == 0):
				return uniqueID


	#Choices
	TYPES = [
					('0' , 'Police Review Boards and Commissions'),
					('1' , 'Sheriff Review Boards and Commissions')
			]

	# Profile:
	name = models.CharField('Name' , max_length = 150)
	type = models.CharField('Type' , max_length = 4 , choices = TYPES , default = '0')
	website = models.URLField('Website URL' , max_length = 300 , blank = True)

	# Location:
	country = models.CharField('Country' , max_length = 3 , choices = COUNTRIES , default = 'USA')
	stateTerritoryProvince = models.CharField('State/Territory/Province' , max_length = 6 , choices = STATES_TERRITORIES_PROVINCES , default = 'USA-CA')
	cityTown = models.CharField('City/Town' , max_length = 60 , blank = True)
	postalCode = models.CharField('Postal Code' , max_length = 15 , blank = True)
	address1 = models.CharField('Address (Line 1)' , max_length = 100 , blank = True)
	address2 = models.CharField('Address (Line 2)' , max_length = 100 , blank = True)

	# General Contact Info:
	email = models.EmailField('Email Address' , blank = True)
	phone = models.CharField('Phone Number (Format: 1-123-555-1234)' , max_length = 18 , blank = True)
	phoneTDD = models.CharField('TTD/TTY Phone Number (Format: 1-123-555-1234)' , max_length = 18 , blank = True)
	fax = models.CharField('Fax Number (Format: 1-123-555-1234)' , max_length = 18 , blank = True)
	contactForm = models.URLField('Contact Form URL' , max_length = 300 , blank = True)

	# Press Contact Info:
	pressEmail = models.EmailField('Press Email Address' , blank = True)
	pressPhone = models.CharField('Press Phone Number (Format: 1-123-555-1234)' , max_length = 18 , blank = True)
	pressContactForm = models.URLField('Press Contact Form URL' , max_length = 300 , blank = True)

	# Contents:
	aboutSummary = models.TextField('About/Summary' , max_length = 10000 , blank = True)
	complaintInfo1 = models.URLField('Complaint Information (URL 1)' , max_length = 300 , blank = True)
	complaintInfo2 = models.URLField('Complaint Information (URL 2)' , max_length = 300 , blank = True)
	complaintForm = models.URLField('Complaint Form URL' , max_length = 300 , blank = True)
	membersPage = models.URLField('Members Page URL' , max_length = 300 , blank = True)
	faqPage = models.URLField('FAQ Page URL' , max_length = 300 , blank = True)

	# Administrative:
	commissionID = models.CharField('Commission ID' , max_length = 36 , default = generateUniqueID)
	createdOn = models.DateTimeField('Record Created On' , auto_now_add = True)
	updatedOn = models.DateTimeField('Record Last Updated On' , auto_now = True)
	lastChangedBy = models.CharField('Last Changed By' , max_length = 50 , blank = True)
	toBeDeleted = models.BooleanField('Delete' , default = False)
	daysUntilDeletion = models.IntegerField('Days Until Deletion' , default = 30)
	completed = models.BooleanField('Completed' , default = True)

	# Permissions:
	approved = models.BooleanField('Record Approved' , default = False)
	public = models.BooleanField('Record Public' , default = False)



	# Manage metadata:
	class Meta:
		verbose_name = 'Oversight Commission'
		verbose_name_plural = 'Oversight Commissions'



class Officer(models.Model):
	firstName = models.CharField('First Name(s)' , max_length = 150 , blank = True)
	middleName = models.CharField('Middle Name/Initial' , max_length = 150 , blank = True)
	lastName = models.CharField('Last Name(s)' , max_length = 150 , blank = True)

	# Administrative:
	createdOn = models.DateTimeField('Record Created On' , auto_now_add = True)
	updatedOn = models.DateTimeField('Record Last Updated On' , auto_now = True)
	lastChangedBy = models.CharField('Last Changed By' , max_length = 50 , blank = True)
	toBeDeleted = models.BooleanField('Delete' , default = False)
	daysUntilDeletion = models.IntegerField('Days Until Deletion' , default = 30)

	# Permissions:
	approved = models.BooleanField('Record Approved' , default = False)
	public = models.BooleanField('Record Public' , default = False)



	# Manage metadata:
	class Meta:
		verbose_name = 'Officer'
		verbose_name_plural = 'Officers'



class InvestigativeReport(models.Model):
	# Related Models:
	subjectOfInvestigation = models.ForeignKey(Officer , null = True , on_delete = models.SET_NULL , verbose_name = 'Subject of Investigation (Officer)')

	# Investigator Metadata:
	investigator = models.CharField('Investigator' , max_length = 500 , blank = True)
	license = models.CharField('Investigator License' , max_length = 500 , blank = True)
	investigatorEmployer = models.CharField('Investigator Employer' , max_length = 500 , blank = True)

	# Contents Metadata:
	client = models.CharField('Client' , max_length = 300 , blank = True)
	date = models.DateTimeField('Date' , blank = True)

	# Contents:
	findingsSummary = models.TextField('Summary of Findings' , max_length = 10000 , blank = True)
	conclusion = models.TextField('Conclusion' , max_length = 10000 , blank = True)

	# References:
	fullReportURL = models.URLField('Full Report URL' , max_length = 300 , blank = True)
	fullArchiveURL = models.URLField('Full Archive URL' , max_length = 300 , blank = True)
	originalPRARequestURL = models.URLField('Original PRA Request URL' , max_length = 300 , blank = True)

	# Administrative:
	createdOn = models.DateTimeField('Record Created On' , auto_now_add = True)
	updatedOn = models.DateTimeField('Record Last Updated On' , auto_now = True)
	lastChangedBy = models.CharField('Last Changed By' , max_length = 50 , blank = True)
	toBeDeleted = models.BooleanField('Delete' , default = False)
	daysUntilDeletion = models.IntegerField('Days Until Deletion' , default = 30)

	# Permissions:
	approved = models.BooleanField('Record Approved' , default = False)
	public = models.BooleanField('Record Public' , default = False)



	# Manage metadata:
	class Meta:
		verbose_name = 'Investigative Report'
		verbose_name_plural = 'Investigative Reports'



class InvestigativeReportFinding(models.Model):
	# Choices:
	FINDINGS = [
					('0' , 'Sustained'),
					('1' , 'Not Sustained'),
					('2' , 'Exonerated'),
					('3' , 'Unfounded')
				]

	# Related Models:
	investigativeReport = models.ForeignKey(InvestigativeReport , on_delete = models.CASCADE , verbose_name = 'Investigative Report')

	# Contents:
	findingSummary = models.TextField('Summary of Finding' , max_length = 10000 , blank = True)
	findingBasis = models.CharField('Department Policy/Legal Code' , max_length = 500 , blank = True)
	findingBasisQuote = models.TextField('Policy/Legal Code Quote' , max_length = 10000 , blank = True)
	finding = models.CharField('Finding' , max_length = 2 , choices = FINDINGS , default = '0')

	# Administrative:
	createdOn = models.DateTimeField('Record Created On' , auto_now_add = True)
	updatedOn = models.DateTimeField('Record Last Updated On' , auto_now = True)
	lastChangedBy = models.CharField('Last Changed By' , max_length = 50 , blank = True)
	toBeDeleted = models.BooleanField('Delete' , default = False)
	daysUntilDeletion = models.IntegerField('Days Until Deletion' , default = 30)

	# Permissions:
	approved = models.BooleanField('Record Approved' , default = False)
	public = models.BooleanField('Record Public' , default = False)



	# Manage metadata:
	class Meta:
		verbose_name = 'Investigative Report Finding'
		verbose_name_plural = 'Investigative Report Findings'
