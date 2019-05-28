# -*- coding: utf-8 -*-
"""
Created on Tue May 28 13:36:26 2019

@author: 31162
"""

# -*- coding: utf-8 -*-
"""
Created on Sun May 26 18:55:42 2019

@author: 31162
"""



import os
import json
import urllib.request
import pandas as pd
import time

# This code can be used to scrape details for any startup tracked by CrunchBase

working_directory= str('C:/crunchbase_testing/Final_run')
os.chdir(working_directory) # Change to working directory

api_key = 'd29cceca579ec417b33bb5902853be92' # Research Access to API valid till April 2019; should request CrunchBase (through Prof. Deepa Mani) to extend the access, if required

# Input file for companies' CrunchBase API URL
company_input_data= pd.read_stata(r'Companies_List.dta')

# Tracking time taken for the code
code_start= time.time() 
# Creating list of all companies' CrunchBase API URL
company_url_list=[]
for string in company_input_data.permalink:
    #company_permalink_input = string.split('/organization/')[-1]
    #company_name_lists.append(company_permalink_input)
    company_url= 'https://api.crunchbase.com/v3.1/organizations/{}?user_key={}'.format(string, api_key)
    company_url_list.append(company_url) # List of all companies' CrunchBase API URL

start_index = 5500 # Specify the index of the first company to be scraped from the input list
end_index =5999 # Specify the index of the last company to be scraped from the input list
folder_location_name = str(str(start_index)+' to '+str(end_index))

os.chdir('C:/crunchbase_testing/Final_run'  + '/' + folder_location_name) # For saving outputs in respective folder lcoations

# Declaring all varibales in Error Dataframce
company_url_error =[] # List of urls of all the companies that returned error while scraping
company_url_list = company_url_list[start_index:end_index+1]




# Declaring all the lists in the CompanyDetails data frame
company_uuid= []
company_permalink = []
company_permalink_aliases =[]
company_api_path =[]
company_web_path =[]
company_api_url =[]
company_name =[]
company_also_known_as =[]
company_short_description =[]
company_description =[]
company_profile_image_url =[]
company_primary_role =[]
company_role_company =[]
company_role_investor =[]
company_role_group =[]
company_role_school =[]
company_investor_type =[]
company_founded_on =[]
company_founded_on_trust_code =[]
company_is_closed =[]
company_closed_on =[]
company_closed_on_trust_code =[]
company_num_employees_min =[]
company_num_employees_max =[]
company_stock_exchange =[]
company_stock_symbol =[]
company_total_funding_usd =[]
company_number_of_investments =[]
company_homepage_url =[]
company_contact_email =[]
company_phone_number =[]
company_rank =[]
company_created_at =[]
company_updated_at =[]
company_owned_by_paging_total_items =[]
company_owned_by_owner_type =[]
company_owned_by_owner_uuid =[]
company_owned_by_owner_permalink =[]
company_owned_by_owner_permalink_aliases =[]
company_owned_by_owner_api_path =[]
company_owned_by_owner_web_path =[]
company_owned_by_owner_api_url =[]
company_owned_by_owner_name =[]
company_owned_by_owner_also_known_as =[]
company_owned_by_owner_short_description =[]
company_owned_by_owner_description =[]
company_owned_by_owner_profile_image_url =[]
company_owned_by_owner_primary_role =[]
company_owned_by_owner_role_company =[]
company_owned_by_owner_role_investor =[]
company_owned_by_owner_role_group =[]
company_owned_by_owner_role_school =[]
company_owned_by_owner_investor_type =[]
company_owned_by_owner_founded_on =[]
company_owned_by_owner_founded_on_trust_code =[]
company_owned_by_owner_is_closed =[]
company_owned_by_owner_closed_on =[]
company_owned_by_owner_closed_on_trust_code =[]
company_owned_by_owner_num_employees_min =[]
company_owned_by_owner_num_employees_max =[]
company_owned_by_owner_stock_exchange =[]
company_owned_by_owner_stock_symbol =[]
company_owned_by_owner_total_funding_usd =[]
company_owned_by_owner_number_of_investments =[]
company_owned_by_owner_homepage_url =[]
company_owned_by_owner_contact_email =[]
company_owned_by_owner_phone_number =[]
company_owned_by_owner_rank =[]
company_owned_by_owner_created_at =[]
company_owned_by_owner_updated_at =[]

ipo_paging_total_items= []
ipo_uuid = []
ipo_type = []
ipo_went_public_on= []
ipo_stock_exchange_symbol= []
ipo_stock_symbol= []
ipo_shares_sold= []
ipo_opening_share_price= []
ipo_opening_share_price_currency_code= []
ipo_opening_share_price_usd= []
ipo_opening_valuation= []
ipo_opening_valuation_currency_code= []
ipo_opening_valuation_usd= []
ipo_money_raised= []
ipo_money_raised_currency_code= []
ipo_money_raised_usd= []
ipo_created_at =[]
ipo_updated_at =[]
acquired_by_paging_total_items= []
acquired_by_type =[]
acquired_by_uuid =[]
acquired_by_api_url= []
acquired_by_price= []
acquired_by_price_currency_code= []
acquired_by_price_usd= []
acquired_by_payment_type= []
acquired_by_acquisition_type= []
acquired_by_acquisition_status= []
acquired_by_disposition_of_acquired= []
acquired_by_announced_on= []
acquired_by_completed_on= []
acquired_by_acquirer_type= []
acquired_by_acquirer_uuid= []
acquired_by_acquirer_name= []
acquired_by_acquirer_also_known_as= []
acquired_by_acquirer_short_description= []
acquired_by_acquirer_description= []
acquired_by_acquirer_profile_image_url= []
acquired_by_acquirer_primary_role= []
acquired_by_acquirer_role_company= []
acquired_by_acquirer_role_investor= []
acquired_by_acquirer_role_group= []
acquired_by_acquirer_role_school= []
acquired_by_acquirer_investor_type= []
acquired_by_acquirer_founded_on= []
acquired_by_acquirer_is_closed= []
acquired_by_acquirer_closed_on= []
acquired_by_acquirer_num_employees_min= []
acquired_by_acquirer_num_employees_max= []
acquired_by_acquirer_stock_exchange= []
acquired_by_acquirer_stock_symbol= []
acquired_by_acquirer_total_funding_usd= []
acquired_by_acquirer_number_of_investments= []
acquired_by_acquirer_homepage_url= []
acquired_by_acquirer_contact_email= []
acquired_by_acquirer_phone_number= []

# Declaring all the lists in the CompanyFunding data frame
company_fundings_url =[]
company_uuid_funding =[]
company_name_funding =[]
funding_type =[]
funding_uuid =[]
funding_announced_on =[]
funding_permalink =[]
funding_api_path =[]
funding_web_path =[]
funding_api_url =[]
funding_funding_type =[]
funding_series =[]
funding_series_qualifier =[]    
funding_announced_on =[]
funding_announced_on_trust_code =[]
funding_closed_on =[]
funding_closed_on_trust_code =[]      
funding_funding_money_raised =[]
funding_money_raised_currency_code =[]
funding_money_raised_usd =[]
funding_target_money_raised =[]
funding_target_money_raised_currency_code =[]
funding_target_money_raised_usd =[]
funding_pre_money_valuation =[]
funding_pre_money_valuation_currency_code =[]
funding_pre_money_valuation_usd =[]
funding_rank =[]
funding_created_at =[]
funding_updated_at =[]

# Declaring all the lists in the CompanyFunding_Investors data frame
company_funding_url =[]
company_uuid_funding_investor =[]
company_name_funding_investor =[]
funding_type_funding_investor =[]
funding_uuid_funding_investor =[]
funding_permalink_funding_investor =[]
funding_api_path_funding_investor =[]
funding_web_path_funding_investor =[]
funding_api_url_funding_investor =[]
funding_funding_type_funding_investor =[]
funding_series_funding_investor =[]
funding_series_qualifier_funding_investor =[]
funding_announced_on_funding_investor =[]
funding_announced_on_trust_code_funding_investor =[]
funding_closed_on_funding_investor =[]
funding_closed_on_trust_code_funding_investor =[]
funding_funding_money_raised_funding_investor =[]
funding_money_raised_currency_code_funding_investor =[]
funding_money_raised_usd_funding_investor =[]
funding_target_money_raised_funding_investor =[]
funding_target_money_raised_currency_code_funding_investor =[]
funding_target_money_raised_usd_funding_investor =[]
funding_pre_money_valuation_funding_investor =[]
funding_pre_money_valuation_currency_code_funding_investor =[]
funding_pre_money_valuation_usd_funding_investor =[]
funding_rank_funding_investor =[]
funding_created_at_funding_investor =[]
funding_updated_at_funding_investor =[]
funding_investor_type =[]
funding_investor_uuid =[]
funding_investor_permalink =[]
funding_investor_permalink_aliases =[]
funding_investor_api_path =[]
funding_investor_web_path =[]
funding_investor_api_url =[]
funding_investor_name =[]
funding_investor_also_known_as =[]
funding_investor_short_description =[]
funding_investor_description =[]
funding_investor_profile_image_url =[]
funding_investor_primary_role =[]
funding_investor_role_company =[]
funding_investor_role_investor =[]
funding_investor_role_group =[]
funding_investor_role_school =[]
funding_investor_investor_type =[]
funding_investor_founded_on =[]
funding_investor_founded_on_trust_code =[]
funding_investor_is_closed =[]
funding_investor_closed_on =[]
funding_investor_closed_on_trust_code =[]
funding_investor_num_employees_min =[]
funding_investor_num_employees_max =[]
funding_investor_stock_exchange =[]
funding_investor_stock_symbol =[]
funding_investor_total_funding_usd =[]
funding_investor_number_of_investments =[]
funding_investor_homepage_url =[]
funding_investor_contact_email =[]
funding_investor_phone_number =[]
funding_investor_rank =[]
funding_investor_created_at =[]
funding_investor_updated_at =[]
funding_investor_first_name =[]
funding_investor_last_name =[]
funding_investor_gender =[]
funding_investor_bio =[]
funding_investor_born_on =[]
funding_investor_born_on_trust_code =[]
funding_investor_died_on =[]
funding_investor_died_on_trust_code =[]
funding_investor_money_invested =[]
funding_investor_money_invested_currency_code = []
funding_investor_money_invested_usd =[]
funding_investor_is_lead_investor =[]

# Declaring all the lists in the CompanyFunding_Investors_Partners data frame
company_uuid_funding_investor_partner =[]
company_name_funding_investor_partner =[]
funding_type_funding_investor_partner =[]
funding_uuid_funding_investor_partner =[]
funding_investor_uuid_investor_partner =[]
funding_funding_type_funding_investor_partner =[]
funding_series_funding_investor_partner =[]
funding_announced_on_funding_investor_partner =[]
funding_investor_partner_type =[]
funding_investor_partner_uuid =[]
funding_investor_partner_permalink =[]
funding_investor_partner_permalink_aliases =[]
funding_investor_partner_api_path =[]
funding_investor_partner_web_path =[]
funding_investor_partner_api_url =[]
funding_investor_partner_first_name =[]
funding_investor_partner_last_name =[]
funding_investor_partner_gender =[]
funding_investor_partner_also_known_as =[]
funding_investor_partner_bio =[]
funding_investor_partner_profile_image_url =[]
funding_investor_partner_role_investor =[]
funding_investor_partner_born_on =[]
funding_investor_partner_born_on_trust_code =[]
funding_investor_partner_died_on =[]
funding_investor_partner_died_on_trust_code =[]
funding_investor_partner_rank =[]
funding_investor_partner_created_at =[]
funding_investor_partner_updated_at =[] 

# Declaring all the lists in the CompanyAcquisitions data frame
company_acquisition_url =[]
company_uuid_acquisition =[]
company_name_acquisition =[]
acquisition_type =[]
acquisition_uuid =[]
acquisition_announced_on =[]
acquisition_permalink =[]
acquisition_api_path =[]
acquisition_web_path =[]
acquisition_api_url =[]
acquisition_price =[]
acquisition_price_currency_code =[]
acquisition_price_usd =[]
acquisition_payment_type =[]
acquisition_acquisition_type =[]
acquisition_acquisition_status =[]
acquisition_disposition_of_acquired =[]
acquisition_announced_on =[]
acquisition_announced_on_trust_code =[]
acquisition_completed_on =[]
acquisition_completed_on_trust_code =[]
acquisition_rank =[]
acquisition_created_at =[]
acquisition_updated_at =[]
target_type =[]
target_uuid =[]
target_permalink = []
target_permalink_aliases =[]
target_api_path =[]
target_web_path =[]
target_api_url =[]
target_name =[]
target_also_known_as =[]
target_short_description =[]
target_description =[]
target_profile_image_url =[]
target_primary_role =[]
target_role_company =[]
target_role_investor =[]
target_role_group =[]
target_role_school =[]
target_investor_type =[]
target_founded_on =[]
target_founded_on_trust_code =[]
target_is_closed =[]
target_closed_on =[]
target_closed_on_trust_code =[]
target_num_employees_min =[]
target_num_employees_max =[]
target_stock_exchange =[]
target_stock_symbol =[]
target_total_funding_usd =[]
target_number_of_investments =[]
target_homepage_url =[]
target_contact_email =[]
target_phone_number =[]
target_rank =[]
target_created_at =[]
target_updated_at =[]

# Declaring all the lists in the CompanyOffices data frame
company_offices_total_items =[]
company_uuid_offices =[]
company_name_offices=[]
company_office_type =[]
company_office_uuid =[]
company_office_street_1 =[]
company_office_street_2 =[]
company_office_postal_code =[]
company_office_city =[]
company_office_region =[]
company_office_country =[]
company_office_city_web_path =[]
company_office_region_code2 =[]
company_office_region_web_path =[]
company_office_country_code2 =[]
company_office_country_code3 =[]
company_office_country_web_path =[]
company_office_latitude =[]
company_office_longitude =[]
company_office_created_at =[]
company_office_updated_at =[]

# Declaring all the lists in the CompanyOffices data frame
company_headquarters_total_items = []
company_uuid_headquarters =[]
company_name_headquarters =[]
company_headquarters_type =[]
company_headquarters_uuid =[]
company_headquarters_name =[]
company_headquarters_street_1 =[]
company_headquarters_street_2 =[]
company_headquarters_postal_code =[]
company_headquarters_city =[]
company_headquarters_region =[]
company_headquarters_country =[]
company_headquarters_city_web_path =[]
company_headquarters_region_code2 =[]
company_headquarters_region_web_path =[]
company_headquarters_country_code2 =[]
company_headquarters_country_code3 =[]
company_headquarters_country_web_path =[]
company_headquarters_latitude =[]
company_headquarters_longitude =[]
company_headquarters_created_at =[]
company_headquarters_updated_at =[]

# Declaring all the lists in the CompanySubOrganizations data frame
company_sub_organizations_url =[]
company_uuid_sub_organizations =[]
company_name_sub_organizations =[]
sub_organization_type =[]
sub_organization_uuid =[]
sub_organization_permalink =[]
sub_organization_permalink_aliases =[]
sub_organization_api_path =[]
sub_organization_web_path =[]
sub_organization_api_url =[]
sub_organization_name =[]
sub_organization_also_known_as =[]
sub_organization_short_description =[]
sub_organization_description =[]
sub_organization_profile_image_url =[]
sub_organization_primary_role =[]
sub_organization_role_company =[]
sub_organization_role_investor =[]
sub_organization_role_group =[]
sub_organization_role_school =[]
sub_organization_investor_type =[]
sub_organization_founded_on =[]
sub_organization_founded_on_trust_code =[]
sub_organization_is_closed =[]
sub_organization_closed_on  =[]
sub_organization_closed_on_trust_code =[]
sub_organization_num_employees_min =[]
sub_organization_num_employees_max =[]
sub_organization_stock_exchange =[]
sub_organization_stock_symbol =[]
sub_organization_total_funding_usd =[]
sub_organization_number_of_investments =[]
sub_organization_homepage_url =[]
sub_organization_contact_email =[]
sub_organization_phone_number =[]
sub_organization_rank =[]
sub_organization_created_at =[]
sub_organization_updated_at =[]

# Declaring all the lists in the CompanyFounders data frame
company_founders_url =[]
company_uuid_founder =[]
company_name_founder =[]
founder_type =[]
founder_uuid =[]
founder_permalink =[]
founder_api_path =[]
founder_web_path =[]
founder_api_url =[]
founder_first_name =[]
founder_last_name =[]
founder_gender =[]
founder_also_known_as =[]
founder_bio =[]
founder_profile_image_url =[]
founder_role_investor =[]
founder_born_on =[]
founder_born_on_trust_code =[]
founder_died_on =[]
founder_died_on_trust_code =[]
founder_rank =[]
founder_created_at =[]
founder_updated_at =[]
founder_primary_location_total_items =[]
founder_primary_location_type =[]
founder_primary_location_uuid =[]
founder_primary_location_location_type =[]
founder_primary_location_parent_location_uuid =[]
founder_primary_location_city =[]
founder_primary_location_region =[]
founder_primary_location_region_code2 =[]
founder_primary_location_country =[]
founder_primary_location_country_code2 =[]
founder_primary_location_country_code3 =[]
founder_primary_location_continent =[]
founder_primary_location_created_at =[]
founder_primary_location_updated_at =[]
founder_primary_affiliation_total_items =[]
founder_primary_affiliation_type =[]
founder_primary_affiliation_uuid =[]
founder_primary_affiliation_title =[]
founder_primary_affiliation_started_on =[]
founder_primary_affiliation_started_on_trust_code =[]
founder_primary_affiliation_ended_on =[]
founder_primary_affiliation_ended_on_trust_code =[]       
founder_primary_affiliation_is_current =[]
founder_primary_affiliation_job_type =[]
founder_primary_affiliation_created_at =[]
founder_primary_affiliation_updated_at =[]
founder_primary_affiliation_organization_type =[]
founder_primary_affiliation_organization_uuid =[]
founder_primary_affiliation_organization_permalink =[]
founder_primary_affiliation_organization_permalink_aliases =[]
founder_primary_affiliation_organization_api_path =[]
founder_primary_affiliation_organization_web_path =[]
founder_primary_affiliation_organization_api_url =[]
founder_primary_affiliation_organization_name =[]
founder_primary_affiliation_organization_also_known_as =[]
founder_primary_affiliation_organization_short_description =[]
founder_primary_affiliation_organization_description =[]
founder_primary_affiliation_organization_profile_image_url =[]
founder_primary_affiliation_organization_primary_role =[]
founder_primary_affiliation_organization_role_company =[]
founder_primary_affiliation_organization_role_investor =[]
founder_primary_affiliation_organization_role_group =[]
founder_primary_affiliation_organization_role_school =[]
founder_primary_affiliation_organization_investor_type =[]
founder_primary_affiliation_organization_founded_on =[]
founder_primary_affiliation_organization_founded_on_trust_code =[]
founder_primary_affiliation_organization_is_closed =[]
founder_primary_affiliation_organization_closed_on =[]
founder_primary_affiliation_organization_closed_on_trust_code =[]
founder_primary_affiliation_organization_num_employees_min =[]
founder_primary_affiliation_organization_num_employees_max =[]
founder_primary_affiliation_organization_stock_exchange =[]
founder_primary_affiliation_organization_stock_symbol =[]
founder_primary_affiliation_organization_total_funding_usd =[]
founder_primary_affiliation_organization_number_of_investments =[]
founder_primary_affiliation_organization_homepage_url =[]
founder_primary_affiliation_organization_contact_email =[]
founder_primary_affiliation_organization_phone_number =[]
founder_primary_affiliation_organization_rank =[]
founder_primary_affiliation_organization_created_at =[]
founder_primary_affiliation_organization_updated_at =[]
founder_primary_image_total_items =[]
founder_primary_image_type =[]
founder_primary_image_uuid =[]
founder_primary_image_asset_path =[]
founder_primary_image_asset_url =[]
founder_primary_image_content_type =[]
founder_primary_image_height =[]
founder_primary_image_width =[]
founder_primary_image_filesize =[]
founder_primary_image_created_at =[]
founder_primary_image_updated_at =[]

# Declaring all the lists in the CompanyFounders_Degrees data frame
company_uuid_founder_degree =[]
company_name_founder_degree =[]
founder_uuid_founder_degree =[]
founder_first_name_founder_degree =[]
founder_last_name_founder_degree =[]
founder_degree_type =[]
founder_degree_uuid =[]
founder_degree_started_on =[]
founder_degree_started_on_trust_code =[]
founder_degree_completed_on =[]
founder_degree_completed_on_trust_code =[]
founder_degree_type_name =[]
founder_degree_subject =[]
founder_degree_created_at =[]
founder_degree_updated_at =[]
founder_degree_school_type =[]
founder_degree_school_uuid =[]
founder_degree_school_permalink =[]
founder_degree_school_permalink_aliases =[]
founder_degree_school_api_path =[]
founder_degree_school_web_path =[]
founder_degree_school_api_url =[]
founder_degree_school_name =[]
founder_degree_school_also_known_as =[]
founder_degree_school_short_description =[]
founder_degree_school_description =[]
founder_degree_school_profile_image_url =[]
founder_degree_school_primary_role =[]
founder_degree_school_role_company =[]
founder_degree_school_role_investor =[]
founder_degree_school_role_group =[]
founder_degree_school_role_school =[]
founder_degree_school_investor_type =[]
founder_degree_school_founded_on =[]
founder_degree_school_founded_on_trust_code =[]
founder_degree_school_is_closed =[]
founder_degree_school_closed_on =[]
founder_degree_school_closed_on_trust_code =[]
founder_degree_school_num_employees_min =[]
founder_degree_school_num_employees_max =[]
founder_degree_school_stock_exchange =[]
founder_degree_school_stock_symbol =[]
founder_degree_school_total_funding_usd =[]
founder_degree_school_number_of_investments =[]
founder_degree_school_homepage_url =[]
founder_degree_school_contact_email =[]
founder_degree_school_phone_number =[]
founder_degree_school_rank =[]
founder_degree_school_created_at =[]
founder_degree_school_updated_at =[]

# Declaring all the lists in the CompanyFounders_Jobs data frame
company_uuid_founder_job =[]
company_name_founder_job =[]
founder_uuid_founder_job =[]
founder_first_name_founder_job =[]
founder_last_name_founder_job =[]
founder_job_type =[]
founder_job_uuid =[]
founder_job_title =[]
founder_job_started_on =[]
founder_job_started_on_trust_code =[]
founder_job_ended_on =[]
founder_job_ended_on_trust_code =[]
founder_job_is_current =[]
founder_job_job_type =[]
founder_job_created_at =[]
founder_job_updated_at =[]
founder_job_organization_type =[]
founder_job_organization_uuid =[]
founder_job_organization_permalink =[]
founder_job_organization_permalink_aliases =[]
founder_job_organization_api_path =[]
founder_job_organization_web_path =[]
founder_job_organization_api_url =[]
founder_job_organization_name =[]
founder_job_organization_also_known_as =[]
founder_job_organization_short_description =[]
founder_job_organization_description =[]
founder_job_organization_profile_image_url =[]
founder_job_organization_primary_role =[]
founder_job_organization_role_company =[]
founder_job_organization_role_investor =[]
founder_job_organization_role_group =[]
founder_job_organization_role_school =[]
founder_job_organization_investor_type =[]
founder_job_organization_founded_on =[]
founder_job_organization_founded_on_trust_code =[]
founder_job_organization_is_closed =[]
founder_job_organization_closed_on =[]
founder_job_organization_closed_on_trust_code =[]
founder_job_organization_num_employees_min =[]
founder_job_organization_num_employees_max =[]
founder_job_organization_stock_exchange =[]
founder_job_organization_stock_symbol =[]
founder_job_organization_total_funding_usd =[]
founder_job_organization_number_of_investments =[]
founder_job_organization_homepage_url =[]
founder_job_organization_contact_email =[]
founder_job_organization_phone_number =[]
founder_job_organization_rank =[]
founder_job_organization_created_at =[]
founder_job_organization_updated_at =[]

# Declaring all the lists in the CompanyFounders_FoundedCompanies data frame
company_uuid_founder_founded_company =[]
company_name_founder_founded_company =[]
founder_uuid_founder_founded_company =[]
founder_first_name_founder_founded_company =[]
founder_last_name_founder_founded_company =[]
founder_founded_company_type =[]
founder_founded_company_uuid =[]
founder_founded_company_permalink =[]
founder_founded_company_permalink_aliases =[]
founder_founded_company_api_path =[]
founder_founded_company_web_path =[]
founder_founded_company_api_url =[]
founder_founded_company_name =[]
founder_founded_company_also_known_as =[]
founder_founded_company_short_description =[]
founder_founded_company_description =[]
founder_founded_company_profile_image_url =[]
founder_founded_company_primary_role =[]
founder_founded_company_role_company =[]
founder_founded_company_role_investor =[]
founder_founded_company_role_group =[]
founder_founded_company_role_school =[]
founder_founded_company_investor_type =[]
founder_founded_company_founded_on =[]
founder_founded_company_founded_on_trust_code =[]
founder_founded_company_is_closed =[]
founder_founded_company_closed_on =[]
founder_founded_company_closed_on_trust_code =[]
founder_founded_company_num_employees_min =[]
founder_founded_company_num_employees_max =[]
founder_founded_company_stock_exchange =[]
founder_founded_company_stock_symbol =[]
founder_founded_company_total_funding_usd =[]
founder_founded_company_number_of_investments =[]
founder_founded_company_homepage_url =[]
founder_founded_company_contact_email =[]
founder_founded_company_phone_number =[]
founder_founded_company_rank =[]
founder_founded_company_created_at =[]
founder_founded_company_updated_at =[]

# Declaring all the lists in the CompanyFounders_Websites data frame
founder_website_paging_total_items =[]
company_uuid_founder_website =[]
company_name_founder_website =[]
founder_uuid_founder_website =[]
founder_first_name_founder_website=[]
founder_last_name_founder_website =[]
founder_website_type=[]
founder_website_uuid=[]
founder_website_website_type=[]
founder_website_website_name=[]
founder_website_url=[]
founder_website_created_at=[]
founder_website_updated_at=[]

# Declaring all the lists in the CompanyFounders_AdvisoryRoles data frame
founder_advisory_roles_paging_total_items =[]
company_uuid_founder_advisory_role = []
company_name_founder_advisory_role = []
founder_uuid_founder_advisory_role = []
founder_first_name_founder_advisory_role = []
founder_last_name_founder_advisory_role = []
founder_advisory_role_type = []
founder_advisory_role_uuid = []
founder_advisory_role_title = []
founder_advisory_role_started_on = []
founder_advisory_role_started_on_trust_code = []
founder_advisory_role_ended_on = []
founder_advisory_role_ended_on_trust_code = []
founder_advisory_role_is_current = []
founder_advisory_role_job_type = []
founder_advisory_role_created_at = []
founder_advisory_role_updated_at = []
founder_advisory_role_organization_permalink = []
founder_advisory_role_organization_permalink_aliases = []
founder_advisory_role_organization_api_path = []
founder_advisory_role_organization_web_path = []
founder_advisory_role_organization_api_url = []
founder_advisory_role_organization_name = []
founder_advisory_role_organization_also_known_as = []
founder_advisory_role_organization_short_description = []
founder_advisory_role_organization_description = []
founder_advisory_role_organization_profile_image_url = []
founder_advisory_role_organization_primary_role = []
founder_advisory_role_organization_role_company = []
founder_advisory_role_organization_role_investor = []
founder_advisory_role_organization_role_group = []
founder_advisory_role_organization_role_school = []
founder_advisory_role_organization_investor_type = []
founder_advisory_role_organization_founded_on = []
founder_advisory_role_organization_founded_on_trust_code = []
founder_advisory_role_organization_is_closed = []
founder_advisory_role_organization_closed_on = []
founder_advisory_role_organization_closed_on_trust_code = []
founder_advisory_role_organization_num_employees_min = []
founder_advisory_role_organization_num_employees_max = []
founder_advisory_role_organization_stock_exchange = []
founder_advisory_role_organization_stock_symbol = []
founder_advisory_role_organization_total_funding_usd = []
founder_advisory_role_organization_number_of_investments = []
founder_advisory_role_organization_homepage_url = []
founder_advisory_role_organization_contact_email = []
founder_advisory_role_organization_phone_number = []
founder_advisory_role_organization_rank = []
founder_advisory_role_organization_created_at = []
founder_advisory_role_organization_updated_at = []

# Declaring all the lists in the CompanyFounders_Investments data frame
founder_investments_paging_total_items =[]
company_uuid_founder_investments =[]
company_name_founder_investments =[]
founder_uuid_founder_investments =[]
founder_first_name_investments =[]
founder_last_name_founder_investments =[]
founder_investment_type =[]
founder_investment_uuid =[]
founder_investment_money_invested =[]
founder_investment_money_invested_currency_code =[]
founder_investment_money_invested_usd =[]
founder_investment_is_lead_investor =[]
founder_investment_announced_on =[]
founder_investment_announced_on_trust_code =[]
founder_investment_created_at =[]
founder_investment_updated_at =[]
founder_investment_funding_round_type =[]
founder_investment_funding_round_uuid =[]
founder_investment_funding_round_permalink =[]
founder_investment_funding_round_api_path =[]
founder_investment_funding_round_web_path =[]
founder_investment_funding_round_api_url =[]
founder_investment_funding_round_funding_type =[]
founder_investment_funding_round_series =[]
founder_investment_funding_round_series_qualifier =[]
founder_investment_funding_round_announced_on =[]
founder_investment_funding_round_announced_on_trust_code =[]
founder_investment_funding_round_closed_on =[]
founder_investment_funding_round_closed_on_trust_code =[]
founder_investment_funding_money_raised =[]
founder_investment_funding_round_money_raised_currency_code =[]
founder_investment_funding_round_money_raised_usd =[]
founder_investment_funding_round_target_money_raised =[]
founder_investment_funding_round_target_money_raised_currency_code =[]
founder_investment_funding_round_target_money_raised_usd =[]
founder_investment_funding_round_pre_money_valuation =[]
founder_investment_funding_round_pre_money_valuation_currency_code =[]
founder_investment_funding_round_pre_money_valuation_usd =[]
founder_investment_funding_round_rank =[]
founder_investment_funding_round_created_at =[]
founder_investment_funding_round_updated_at =[]
founder_investment_funding_round_funded_organization_type =[]
founder_investment_funding_round_funded_organization_uuid =[]
founder_investment_funding_round_funded_organization_permalink =[]
founder_investment_funding_round_funded_organization_permalink_aliases =[]
founder_investment_funding_round_funded_organization_api_path =[]
founder_investment_funding_round_funded_organization_web_path =[]
founder_investment_funding_round_funded_organization_api_url =[]
founder_investment_funding_round_funded_organization_name =[]
founder_investment_funding_round_funded_organization_also_known_as =[]
founder_investment_funding_round_funded_organization_short_description =[]
founder_investment_funding_round_funded_organization_description =[]
founder_investment_funding_round_funded_organization_profile_image_url =[]
founder_investment_funding_round_funded_organization_primary_role =[]
founder_investment_funding_round_funded_organization_role_company =[]
founder_investment_funding_round_funded_organization_role_investor =[]
founder_investment_funding_round_funded_organization_role_group =[]
founder_investment_funding_round_funded_organization_role_school =[]
founder_investment_funding_round_funded_organization_investor_type =[]
founder_investment_funding_round_funded_organization_founded_on =[]
founder_investment_funding_round_funded_organization_founded_on_trust_code =[]
founder_investment_funding_round_funded_organization_is_closed =[]
founder_investment_funding_round_funded_organization_closed_on =[]
founder_investment_funding_round_funded_organization_closed_on_trust_code =[]
founder_investment_funding_round_funded_organization_num_employees_min =[]
founder_investment_funding_round_funded_organization_num_employees_max =[]
founder_investment_funding_round_funded_organization_stock_exchange =[]
founder_investment_funding_round_funded_organization_stock_symbol =[]
founder_investment_funding_round_funded_organization_total_funding_usd =[]
founder_investment_funding_round_funded_organization_number_of_investments =[]
founder_investment_funding_round_funded_organization_homepage_url =[]
founder_investment_funding_round_funded_organization_contact_email =[]
founder_investment_funding_round_funded_organization_phone_number =[]
founder_investment_funding_round_funded_organization_rank =[]
founder_investment_funding_round_funded_organization_created_at =[]
founder_investment_funding_round_funded_organization_updated_at =[]






# Declaring all the lists in the Company_BoardMembers data frame
company_uuid_board_details=[]
company_name_board_details=[]
board_details_uuid=[]
board_details_title=[]
board_details_started_on=[]
board_details_started_on_trust_code=[]
board_details_ended_on=[]
board_details_ended_on_trust_code=[]
board_details_is_current=[]
board_details_job_type=[]
board_details_created_at=[]
board_details_updated_at=[]
board_details_type=[]
board_details_person_uuid=[]
board_details_person_permalink=[]
board_details_person_permalink_aliases=[]
board_details_person_api_path=[]
board_details_person_web_path=[]
board_details_person_api_url=[]
board_details_person_first_name=[]
board_details_person_last_name=[]
board_details_person_gender=[]
board_details_person_also_known_as=[]
board_details_person_bio=[]
board_details_person_profile_image_url=[]
board_details_person_role_investor=[]
board_details_person_born_on=[]
board_details_person_born_on_trust_code=[]
board_details_person_died_on=[]
board_details_person_died_on_trust_code=[]
board_details_person_rank=[]
board_details_person_created_at=[]
board_details_person_updated_at=[]
BoardMembers_primary_location_total_items =[]
BoardMembers_primary_location_type =[]
BoardMembers_primary_location_uuid =[]
BoardMembers_primary_location_location_type =[]
BoardMembers_primary_location_parent_location_uuid =[]
BoardMembers_primary_location_city =[]
BoardMembers_primary_location_region =[]
BoardMembers_primary_location_region_code2 =[]
BoardMembers_primary_location_country =[]
BoardMembers_primary_location_country_code2 =[]
BoardMembers_primary_location_country_code3 =[]
BoardMembers_primary_location_continent =[]
BoardMembers_primary_location_created_at =[]
BoardMembers_primary_location_updated_at =[]
BoardMembers_primary_affiliation_total_items =[]
BoardMembers_primary_affiliation_type =[]
BoardMembers_primary_affiliation_uuid =[]
BoardMembers_primary_affiliation_title =[]
BoardMembers_primary_affiliation_started_on =[]
BoardMembers_primary_affiliation_started_on_trust_code =[]
BoardMembers_primary_affiliation_ended_on =[]
BoardMembers_primary_affiliation_ended_on_trust_code =[]       
BoardMembers_primary_affiliation_is_current =[]
BoardMembers_primary_affiliation_job_type =[]
BoardMembers_primary_affiliation_created_at =[]
BoardMembers_primary_affiliation_updated_at =[]
BoardMembers_primary_affiliation_organization_type =[]
BoardMembers_primary_affiliation_organization_uuid =[]
BoardMembers_primary_affiliation_organization_permalink =[]
BoardMembers_primary_affiliation_organization_permalink_aliases =[]
BoardMembers_primary_affiliation_organization_api_path =[]
BoardMembers_primary_affiliation_organization_web_path =[]
BoardMembers_primary_affiliation_organization_api_url =[]
BoardMembers_primary_affiliation_organization_name =[]
BoardMembers_primary_affiliation_organization_also_known_as =[]
BoardMembers_primary_affiliation_organization_short_description =[]
BoardMembers_primary_affiliation_organization_description =[]
BoardMembers_primary_affiliation_organization_profile_image_url =[]
BoardMembers_primary_affiliation_organization_primary_role =[]
BoardMembers_primary_affiliation_organization_role_company =[]
BoardMembers_primary_affiliation_organization_role_investor =[]
BoardMembers_primary_affiliation_organization_role_group =[]
BoardMembers_primary_affiliation_organization_role_school =[]
BoardMembers_primary_affiliation_organization_investor_type =[]
BoardMembers_primary_affiliation_organization_founded_on =[]
BoardMembers_primary_affiliation_organization_founded_on_trust_code =[]
BoardMembers_primary_affiliation_organization_is_closed =[]
BoardMembers_primary_affiliation_organization_closed_on =[]
BoardMembers_primary_affiliation_organization_closed_on_trust_code =[]
BoardMembers_primary_affiliation_organization_num_employees_min =[]
BoardMembers_primary_affiliation_organization_num_employees_max =[]
BoardMembers_primary_affiliation_organization_stock_exchange =[]
BoardMembers_primary_affiliation_organization_stock_symbol =[]
BoardMembers_primary_affiliation_organization_total_funding_usd =[]
BoardMembers_primary_affiliation_organization_number_of_investments =[]
BoardMembers_primary_affiliation_organization_homepage_url =[]
BoardMembers_primary_affiliation_organization_contact_email =[]
BoardMembers_primary_affiliation_organization_phone_number =[]
BoardMembers_primary_affiliation_organization_rank =[]
BoardMembers_primary_affiliation_organization_created_at =[]
BoardMembers_primary_affiliation_organization_updated_at =[]
BoardMembers_primary_image_total_items =[]
BoardMembers_primary_image_type =[]
BoardMembers_primary_image_uuid =[]
BoardMembers_primary_image_asset_path =[]
BoardMembers_primary_image_asset_url =[]
BoardMembers_primary_image_content_type =[]
BoardMembers_primary_image_height =[]
BoardMembers_primary_image_width =[]
BoardMembers_primary_image_filesize =[]
BoardMembers_primary_image_created_at =[]
BoardMembers_primary_image_updated_at =[]
# Declaring all the lists in the Company_BoardMembers_Degrees data frame
company_uuid_BoardMembers_degree =[]
company_name_BoardMembers_degree =[]
BoardMembers_uuid_BoardMembers_degree =[]
BoardMembers_first_name_BoardMembers_degree =[]
BoardMembers_last_name_BoardMembers_degree =[]
BoardMembers_degree_type =[]
BoardMembers_degree_uuid =[]
BoardMembers_degree_started_on =[]
BoardMembers_degree_started_on_trust_code =[]
BoardMembers_degree_completed_on =[]
BoardMembers_degree_completed_on_trust_code =[]
BoardMembers_degree_type_name =[]
BoardMembers_degree_subject =[]
BoardMembers_degree_created_at =[]
BoardMembers_degree_updated_at =[]
BoardMembers_degree_school_type =[]
BoardMembers_degree_school_uuid =[]
BoardMembers_degree_school_permalink =[]
BoardMembers_degree_school_permalink_aliases =[]
BoardMembers_degree_school_api_path =[]
BoardMembers_degree_school_web_path =[]
BoardMembers_degree_school_api_url =[]
BoardMembers_degree_school_name =[]
BoardMembers_degree_school_also_known_as =[]
BoardMembers_degree_school_short_description =[]
BoardMembers_degree_school_description =[]
BoardMembers_degree_school_profile_image_url =[]
BoardMembers_degree_school_primary_role =[]
BoardMembers_degree_school_role_company =[]
BoardMembers_degree_school_role_investor =[]
BoardMembers_degree_school_role_group =[]
BoardMembers_degree_school_role_school =[]
BoardMembers_degree_school_investor_type =[]
BoardMembers_degree_school_founded_on =[]
BoardMembers_degree_school_founded_on_trust_code =[]
BoardMembers_degree_school_is_closed =[]
BoardMembers_degree_school_closed_on =[]
BoardMembers_degree_school_closed_on_trust_code =[]
BoardMembers_degree_school_num_employees_min =[]
BoardMembers_degree_school_num_employees_max =[]
BoardMembers_degree_school_stock_exchange =[]
BoardMembers_degree_school_stock_symbol =[]
BoardMembers_degree_school_total_funding_usd =[]
BoardMembers_degree_school_number_of_investments =[]
BoardMembers_degree_school_homepage_url =[]
BoardMembers_degree_school_contact_email =[]
BoardMembers_degree_school_phone_number =[]
BoardMembers_degree_school_rank =[]
BoardMembers_degree_school_created_at =[]
BoardMembers_degree_school_updated_at =[]
# Declaring all the lists in the Company_BoardMembers_Jobs data frame
company_uuid_BoardMembers_job =[]
company_name_BoardMembers_job =[]
BoardMembers_uuid_BoardMembers_job =[]
BoardMembers_first_name_BoardMembers_job =[]
BoardMembers_last_name_BoardMembers_job =[]
BoardMembers_job_type =[]
BoardMembers_job_uuid =[]
BoardMembers_job_title =[]
BoardMembers_job_started_on =[]
BoardMembers_job_started_on_trust_code =[]
BoardMembers_job_ended_on =[]
BoardMembers_job_ended_on_trust_code =[]
BoardMembers_job_is_current =[]
BoardMembers_job_job_type =[]
BoardMembers_job_created_at =[]
BoardMembers_job_updated_at =[]
BoardMembers_job_organization_type =[]
BoardMembers_job_organization_uuid =[]
BoardMembers_job_organization_permalink =[]
BoardMembers_job_organization_permalink_aliases =[]
BoardMembers_job_organization_api_path =[]
BoardMembers_job_organization_web_path =[]
BoardMembers_job_organization_api_url =[]
BoardMembers_job_organization_name =[]
BoardMembers_job_organization_also_known_as =[]
BoardMembers_job_organization_short_description =[]
BoardMembers_job_organization_description =[]
BoardMembers_job_organization_profile_image_url =[]
BoardMembers_job_organization_primary_role =[]
BoardMembers_job_organization_role_company =[]
BoardMembers_job_organization_role_investor =[]
BoardMembers_job_organization_role_group =[]
BoardMembers_job_organization_role_school =[]
BoardMembers_job_organization_investor_type =[]
BoardMembers_job_organization_founded_on =[]
BoardMembers_job_organization_founded_on_trust_code =[]
BoardMembers_job_organization_is_closed =[]
BoardMembers_job_organization_closed_on =[]
BoardMembers_job_organization_closed_on_trust_code =[]
BoardMembers_job_organization_num_employees_min =[]
BoardMembers_job_organization_num_employees_max =[]
BoardMembers_job_organization_stock_exchange =[]
BoardMembers_job_organization_stock_symbol =[]
BoardMembers_job_organization_total_funding_usd =[]
BoardMembers_job_organization_number_of_investments =[]
BoardMembers_job_organization_homepage_url =[]
BoardMembers_job_organization_contact_email =[]
BoardMembers_job_organization_phone_number =[]
BoardMembers_job_organization_rank =[]
BoardMembers_job_organization_created_at =[]
BoardMembers_job_organization_updated_at =[]
# Declaring all the lists in the Company_BoardMembers_FoundedCompanies data frame
company_uuid_BoardMembers_founded_company =[]
company_name_BoardMembers_founded_company =[]
BoardMembers_uuid_BoardMembers_founded_company =[]
BoardMembers_first_name_BoardMembers_founded_company =[]
BoardMembers_last_name_BoardMembers_founded_company =[]
BoardMembers_founded_company_type =[]
BoardMembers_founded_company_uuid =[]
BoardMembers_founded_company_permalink =[]
BoardMembers_founded_company_permalink_aliases =[]
BoardMembers_founded_company_api_path =[]
BoardMembers_founded_company_web_path =[]
BoardMembers_founded_company_api_url =[]
BoardMembers_founded_company_name =[]
BoardMembers_founded_company_also_known_as =[]
BoardMembers_founded_company_short_description =[]
BoardMembers_founded_company_description =[]
BoardMembers_founded_company_profile_image_url =[]
BoardMembers_founded_company_primary_role =[]
BoardMembers_founded_company_role_company =[]
BoardMembers_founded_company_role_investor =[]
BoardMembers_founded_company_role_group =[]
BoardMembers_founded_company_role_school =[]
BoardMembers_founded_company_investor_type =[]
BoardMembers_founded_company_founded_on =[]
BoardMembers_founded_company_founded_on_trust_code =[]
BoardMembers_founded_company_is_closed =[]
BoardMembers_founded_company_closed_on =[]
BoardMembers_founded_company_closed_on_trust_code =[]
BoardMembers_founded_company_num_employees_min =[]
BoardMembers_founded_company_num_employees_max =[]
BoardMembers_founded_company_stock_exchange =[]
BoardMembers_founded_company_stock_symbol =[]
BoardMembers_founded_company_total_funding_usd =[]
BoardMembers_founded_company_number_of_investments =[]
BoardMembers_founded_company_homepage_url =[]
BoardMembers_founded_company_contact_email =[]
BoardMembers_founded_company_phone_number =[]
BoardMembers_founded_company_rank =[]
BoardMembers_founded_company_created_at =[]
BoardMembers_founded_company_updated_at =[]
# Declaring all the lists in the Company_BoardMembers_Websites data frame
BoardMembers_website_paging_total_items =[]
company_uuid_BoardMembers_website =[]
company_name_BoardMembers_website =[]
BoardMembers_uuid_BoardMembers_website =[]
BoardMembers_first_name_BoardMembers_website=[]
BoardMembers_last_name_BoardMembers_website =[]
BoardMembers_website_type=[]
BoardMembers_website_uuid=[]
BoardMembers_website_website_type=[]
BoardMembers_website_website_name=[]
BoardMembers_website_url=[]
BoardMembers_website_created_at=[]
BoardMembers_website_updated_at=[]
# Declaring all the lists in the CompanyBoardMembers_AdvisoryRoles data frame
BoardMembers_advisory_roles_paging_total_items =[]
company_uuid_BoardMembers_advisory_role = []
company_name_BoardMembers_advisory_role = []
BoardMembers_uuid_BoardMembers_advisory_role = []
BoardMembers_first_name_BoardMembers_advisory_role = []
BoardMembers_last_name_BoardMembers_advisory_role = []
BoardMembers_advisory_role_type = []
BoardMembers_advisory_role_uuid = []
BoardMembers_advisory_role_title = []
BoardMembers_advisory_role_started_on = []
BoardMembers_advisory_role_started_on_trust_code = []
BoardMembers_advisory_role_ended_on = []
BoardMembers_advisory_role_ended_on_trust_code = []
BoardMembers_advisory_role_is_current = []
BoardMembers_advisory_role_job_type = []
BoardMembers_advisory_role_created_at = []
BoardMembers_advisory_role_updated_at = []
BoardMembers_advisory_role_organization_permalink = []
BoardMembers_advisory_role_organization_permalink_aliases = []
BoardMembers_advisory_role_organization_api_path = []
BoardMembers_advisory_role_organization_web_path = []
BoardMembers_advisory_role_organization_api_url = []
BoardMembers_advisory_role_organization_name = []
BoardMembers_advisory_role_organization_also_known_as = []
BoardMembers_advisory_role_organization_short_description = []
BoardMembers_advisory_role_organization_description = []
BoardMembers_advisory_role_organization_profile_image_url = []
BoardMembers_advisory_role_organization_primary_role = []
BoardMembers_advisory_role_organization_role_company = []
BoardMembers_advisory_role_organization_role_investor = []
BoardMembers_advisory_role_organization_role_group = []
BoardMembers_advisory_role_organization_role_school = []
BoardMembers_advisory_role_organization_investor_type = []
BoardMembers_advisory_role_organization_founded_on = []
BoardMembers_advisory_role_organization_founded_on_trust_code = []
BoardMembers_advisory_role_organization_is_closed = []
BoardMembers_advisory_role_organization_closed_on = []
BoardMembers_advisory_role_organization_closed_on_trust_code = []
BoardMembers_advisory_role_organization_num_employees_min = []
BoardMembers_advisory_role_organization_num_employees_max = []
BoardMembers_advisory_role_organization_stock_exchange = []
BoardMembers_advisory_role_organization_stock_symbol = []
BoardMembers_advisory_role_organization_total_funding_usd = []
BoardMembers_advisory_role_organization_number_of_investments = []
BoardMembers_advisory_role_organization_homepage_url = []
BoardMembers_advisory_role_organization_contact_email = []
BoardMembers_advisory_role_organization_phone_number = []
BoardMembers_advisory_role_organization_rank = []
BoardMembers_advisory_role_organization_created_at = []
BoardMembers_advisory_role_organization_updated_at = []
# Declaring all the lists in the Company_BoardMembers_Investments data frame
BoardMembers_investments_paging_total_items =[]
company_uuid_BoardMembers_investments =[]
company_name_BoardMembers_investments =[]
BoardMembers_uuid_BoardMembers_investments =[]
BoardMembers_first_name_investments =[]
BoardMembers_last_name_BoardMembers_investments =[]
BoardMembers_investment_type =[]
BoardMembers_investment_uuid =[]
BoardMembers_investment_money_invested =[]
BoardMembers_investment_money_invested_currency_code =[]
BoardMembers_investment_money_invested_usd =[]
BoardMembers_investment_is_lead_investor =[]
BoardMembers_investment_announced_on =[]
BoardMembers_investment_announced_on_trust_code =[]
BoardMembers_investment_created_at =[]
BoardMembers_investment_updated_at =[]
BoardMembers_investment_funding_round_type =[]
BoardMembers_investment_funding_round_uuid =[]
BoardMembers_investment_funding_round_permalink =[]
BoardMembers_investment_funding_round_api_path =[]
BoardMembers_investment_funding_round_web_path =[]
BoardMembers_investment_funding_round_api_url =[]
BoardMembers_investment_funding_round_funding_type =[]
BoardMembers_investment_funding_round_series =[]
BoardMembers_investment_funding_round_series_qualifier =[]
BoardMembers_investment_funding_round_announced_on =[]
BoardMembers_investment_funding_round_announced_on_trust_code =[]
BoardMembers_investment_funding_round_closed_on =[]
BoardMembers_investment_funding_round_closed_on_trust_code =[]
BoardMembers_investment_funding_money_raised =[]
BoardMembers_investment_funding_round_money_raised_currency_code =[]
BoardMembers_investment_funding_round_money_raised_usd =[]
BoardMembers_investment_funding_round_target_money_raised =[]
BoardMembers_investment_funding_round_target_money_raised_currency_code =[]
BoardMembers_investment_funding_round_target_money_raised_usd =[]
BoardMembers_investment_funding_round_pre_money_valuation =[]
BoardMembers_investment_funding_round_pre_money_valuation_currency_code =[]
BoardMembers_investment_funding_round_pre_money_valuation_usd =[]
BoardMembers_investment_funding_round_rank =[]
BoardMembers_investment_funding_round_created_at =[]
BoardMembers_investment_funding_round_updated_at =[]
BoardMembers_investment_funding_round_funded_organization_type =[]
BoardMembers_investment_funding_round_funded_organization_uuid =[]
BoardMembers_investment_funding_round_funded_organization_permalink =[]
BoardMembers_investment_funding_round_funded_organization_permalink_aliases =[]
BoardMembers_investment_funding_round_funded_organization_api_path =[]
BoardMembers_investment_funding_round_funded_organization_web_path =[]
BoardMembers_investment_funding_round_funded_organization_api_url =[]
BoardMembers_investment_funding_round_funded_organization_name =[]
BoardMembers_investment_funding_round_funded_organization_also_known_as =[]
BoardMembers_investment_funding_round_funded_organization_short_description =[]
BoardMembers_investment_funding_round_funded_organization_description =[]
BoardMembers_investment_funding_round_funded_organization_profile_image_url =[]
BoardMembers_investment_funding_round_funded_organization_primary_role =[]
BoardMembers_investment_funding_round_funded_organization_role_company =[]
BoardMembers_investment_funding_round_funded_organization_role_investor =[]
BoardMembers_investment_funding_round_funded_organization_role_group =[]
BoardMembers_investment_funding_round_funded_organization_role_school =[]
BoardMembers_investment_funding_round_funded_organization_investor_type =[]
BoardMembers_investment_funding_round_funded_organization_founded_on =[]
BoardMembers_investment_funding_round_funded_organization_founded_on_trust_code =[]
BoardMembers_investment_funding_round_funded_organization_is_closed =[]
BoardMembers_investment_funding_round_funded_organization_closed_on =[]
BoardMembers_investment_funding_round_funded_organization_closed_on_trust_code =[]
BoardMembers_investment_funding_round_funded_organization_num_employees_min =[]
BoardMembers_investment_funding_round_funded_organization_num_employees_max =[]
BoardMembers_investment_funding_round_funded_organization_stock_exchange =[]
BoardMembers_investment_funding_round_funded_organization_stock_symbol =[]
BoardMembers_investment_funding_round_funded_organization_total_funding_usd =[]
BoardMembers_investment_funding_round_funded_organization_number_of_investments =[]
BoardMembers_investment_funding_round_funded_organization_homepage_url =[]
BoardMembers_investment_funding_round_funded_organization_contact_email =[]
BoardMembers_investment_funding_round_funded_organization_phone_number =[]
BoardMembers_investment_funding_round_funded_organization_rank =[]
BoardMembers_investment_funding_round_funded_organization_created_at =[]
BoardMembers_investment_funding_round_funded_organization_updated_at =[]






# Dataframes for companies skipped because of timeout error
timeout_excep_company =[]
timeout_excep_funding_company=[]
timeout_excep_fundings=[]
timeout_excep_investors=[]
timeout_exceptions_acquistions=[]
timeout_except_acquisition=[]
timeout_except_offices=[]
timeout_except_office=[]
timeout_excep_headquarters=[]
timeout_excep_headquarter=[]
time_excep_suborganisations=[]
time_excep_suborganisation=[]
time_excep_company_founders=[]
time_excep_company_founder=[]
timeout_excep_founder_details=[]
time_excep_founders_investment=[]



funding_api_url_check=[]
company_details=[]

index=start_index
timeout_time_seconds= 100 #User-defined timeout timeframe

company_count= 1 # Company Counter for tracking
company_count_error= 0 # Company Error Counter for tracking companies returning error while scraping
# Basic details for each company from each company's CrunchBase API url
for company_url in company_url_list:
    #tracking and printing index
    company_start= time.time()
    
    #tracking index
    print(('current index is {}').format(index))
    index= index+1

    
    try:
        #checking for all urls at first
        #checking url for company
        url= company_url
        response = urllib.request.urlopen(url, timeout=timeout_time_seconds)
        data = json.loads(response.read().decode())
        company_details= data['data']
        #checking URLs for fundings
        fundings_url = company_details['relationships']['funding_rounds']['paging']['first_page_url'] +'?user_key={}'.format(api_key)
        company_funding_url.append(fundings_url)
        response = urllib.request.urlopen(fundings_url, timeout=timeout_time_seconds)
        data_funding = json.loads(response.read().decode())
        funding_paging_number_of_pages= data_funding['data']['paging']['number_of_pages']
        page_fundings=1
        while page_fundings <= funding_paging_number_of_pages: # Pagination - For any item, CrunchBase API shows at most 100 entries per page. For items with over 100 entries, we have to scrape details from each page
            fundings_url = company_details['relationships']['funding_rounds']['paging']['first_page_url'] + '?page={}&sort_order=announced_on%20DESC&items_per_page=100&user_key={}'.format(page_fundings, api_key)
            response = urllib.request.urlopen(fundings_url,timeout=timeout_time_seconds)
            data_fundings = json.loads(response.read().decode())
            page_fundings = page_fundings+1
            if data_fundings['data']['items'][-1]:
                for funding_details in data_fundings['data']['items']:
                    funding_api_url_check.append(funding_details['properties']['api_url'])
                    funding_url_check = funding_api_url_check[-1] + '?&user_key={}'.format(api_key)
                    response = urllib.request.urlopen(funding_url_check, timeout=timeout_time_seconds)
                    data_funding = json.loads(response.read().decode())
                    
        #checking URLs for acquisitions
        acquisition_url = company_details['relationships']['acquisitions']['paging']['first_page_url'] +'?user_key={}'.format(api_key)            
        company_acquisition_url.append(acquisition_url)
        response = urllib.request.urlopen(acquisition_url, timeout=timeout_time_seconds)
        data_acquisition = json.loads(response.read().decode())
        acquisition_paging_number_of_pages= data_acquisition['data']['paging']['number_of_pages']
        page=1
        while page <= acquisition_paging_number_of_pages: # Pagination - For any item, CrunchBase API shows at most 100 entries per page. For items with over 100 entries, we have to scrape details from each page
            acquisition_url = company_details['relationships']['acquisitions']['paging']['first_page_url'] + '?page={}&sort_order=announced_on__value%20DESC&items_per_page=100&user_key={}'.format(page, api_key)
            response = urllib.request.urlopen(acquisition_url, timeout=timeout_time_seconds)
            data_acquisition = json.loads(response.read().decode())
            page = page+1
            offices_url = company_details['relationships']['offices']['paging']['first_page_url'] +'?user_key={}'.format(api_key)
            response = urllib.request.urlopen(offices_url, timeout=timeout_time_seconds)
            data_offices = json.loads(response.read().decode())
            company_offices_paging_number_of_pages= data_offices['data']['paging']['number_of_pages']
            page_offices=1
            while page_offices <= company_offices_paging_number_of_pages:
                offices_url = company_details['relationships']['offices']['paging']['first_page_url'] + '?page={}items_per_page=100&user_key={}'.format(page_offices, api_key)
                response = urllib.request.urlopen(offices_url, timeout=timeout_time_seconds)
                timeout_except_office.append(url)
                data_offices = json.loads(response.read().decode())
                page_offices = page_offices+1
                
        #checking URLs for headquarters
        headquarters_url = company_details['relationships']['headquarters']['paging']['first_page_url'] +'?user_key={}'.format(api_key)
        response = urllib.request.urlopen(headquarters_url, timeout=timeout_time_seconds)
        data_headquarters = json.loads(response.read().decode())
        company_headquarters_paging_number_of_pages= data_headquarters['data']['paging']['number_of_pages']
        page_headquarters=1
        while page_headquarters <= company_headquarters_paging_number_of_pages: # Pagination - For any item, CrunchBase API shows at most 100 entries per page. For items with over 100 entries, we have to scrape details from each page
            headquarters_url = company_details['relationships']['headquarters']['paging']['first_page_url'] + '?page={}items_per_page=100&user_key={}'.format(page_headquarters, api_key)
            response = urllib.request.urlopen(headquarters_url, timeout=timeout_time_seconds)
            response = urllib.request.urlopen(headquarters_url)
            data_headquarters = json.loads(response.read().decode())
            page_headquarters = page_headquarters+1
        
        #checking URLs for sub organisation
        sub_organizations_url = company_details['relationships']['sub_organizations']['paging']['first_page_url'] +'?user_key={}'.format(api_key)
        page_sub_organizations=1
        response = urllib.request.urlopen(sub_organizations_url, timeout=timeout_time_seconds)
        data_sub_organizations = json.loads(response.read().decode())
        sub_organizations_paging_number_of_pages= data_sub_organizations['data']['paging']['number_of_pages']
        page_sub_organizations=1
        while page_sub_organizations <= sub_organizations_paging_number_of_pages: # Pagination - For any item, CrunchBase API shows at most 100 entries per page. For items with over 100 entries, we have to scrape details from each page
            sub_organizations_url = company_details['relationships']['sub_organizations']['paging']['first_page_url'] + '?page={}%20DESC&items_per_page=100&user_key={}'.format(page_sub_organizations, api_key)
            response = urllib.request.urlopen(sub_organizations_url, timeout=timeout_time_seconds)
            data_sub_organizations = json.loads(response.read().decode())
            page_sub_organizations = page_sub_organizations+1
        #checking URLs for founder 
        founders_url = company_details['relationships']['founders']['paging']['first_page_url'] +'?user_key={}'.format(api_key)
        response = urllib.request.urlopen(founders_url, timeout=timeout_time_seconds)
        data_founders = json.loads(response.read().decode())
        founder_paging_number_of_pages= data_founders['data']['paging']['number_of_pages']
        page_founders=1
        while page_founders <= founder_paging_number_of_pages: # Pagination - For any item, CrunchBase API shows at most 100 entries per page. For items with over 100 entries, we have to scrape details from each page
            founders_url = company_details['relationships']['founders']['paging']['first_page_url'] + '?page={}%20DESC&items_per_page=100&user_key={}'.format(page_founders, api_key)
            response = urllib.request.urlopen(founders_url, timeout=timeout_time_seconds)
            data_founders = json.loads(response.read().decode())
            page_founders = page_founders+1
            for founders_details in data_founders['data']['items']:
                founder_url= 'https://api.crunchbase.com/v3.1/people/{}?user_key={}'.format(founders_details['uuid'], api_key)
                response = urllib.request.urlopen(founder_url, timeout=timeout_time_seconds)
                data_founder = json.loads(response.read().decode())
                founder_details = data_founder['data']['relationships']
        

        
        
        
        #checking URLs for board members
        board_url = company_details['relationships']['board_members_and_advisors']['paging']['first_page_url'] +'?user_key={}'.format(api_key)
        response = urllib.request.urlopen(board_url, timeout=timeout_time_seconds)
        data_board = json.loads(response.read().decode())
        BoardMembers_paging_number_of_pages= data_board['data']['paging']['number_of_pages']
        page_board=1
        while page_board <= BoardMembers_paging_number_of_pages: # Pagination - For any item, CrunchBase API shows at most 100 entries per page. For items with over 100 entries, we have to scrape details from each page
            board_url = company_details['relationships']['board_members_and_advisors']['paging']['first_page_url'] + '?page={}%20DESC&items_per_page=100&user_key={}'.format(page_board, api_key)
            response = urllib.request.urlopen(board_url, timeout=timeout_time_seconds)
            data_board = json.loads(response.read().decode())
            page_board = page_board+1
            for board_details in data_board['data']['items']:
                BoardMembers_url= 'https://api.crunchbase.com/v3.1/people/{}?user_key={}'.format(board_details['relationships']['person']['uuid'], api_key) 
                response = urllib.request.urlopen(BoardMembers_url, timeout=timeout_time_seconds)
                data_board_members = json.loads(response.read().decode())
                BoardMembers_details = data_board_members['data']['relationships']     
        
        #checking completed
    
        

                    
    
        
        
        #checking completed        
        
        #code to scrape
        url= company_url
        try:
            response = urllib.request.urlopen(url, timeout=timeout_time_seconds)
        except:
            timeout_excep_company.append(url)
            time.sleep(2)
            continue
            
        #data_founder=[]
        data = json.loads(response.read().decode())
        company_details= data['data']
        # Basic details for each company
        company_uuid.append(company_details['uuid'])
        company_permalink.append(company_details['properties']['permalink'])
        company_permalink_aliases.append(company_details['properties']['permalink_aliases'])
        company_api_path.append(company_details['properties']['api_path'])
        company_web_path.append(company_details['properties']['web_path'])
        company_api_url.append(company_details['properties']['api_url'])
        company_name.append(company_details['properties']['name'])
        company_also_known_as.append(company_details['properties']['also_known_as'])
        company_short_description.append(company_details['properties']['short_description'])
        company_description.append(company_details['properties']['description'])
        company_profile_image_url.append(company_details['properties']['profile_image_url'])
        company_primary_role.append(company_details['properties']['primary_role'])
        company_role_company.append(company_details['properties']['role_company'])
        company_role_investor.append(company_details['properties']['role_investor'])
        company_role_group.append(company_details['properties']['role_group'])
        company_role_school.append(company_details['properties']['role_school'])
        company_investor_type.append(company_details['properties']['investor_type'])
        company_founded_on.append(company_details['properties']['founded_on'])
        company_founded_on_trust_code.append(company_details['properties']['founded_on_trust_code'])
        company_is_closed.append(company_details['properties']['is_closed'])
        company_closed_on.append(company_details['properties']['closed_on'])
        company_closed_on_trust_code.append(company_details['properties']['closed_on_trust_code'])
        company_num_employees_min.append(company_details['properties']['num_employees_min'])
        company_num_employees_max.append(company_details['properties']['num_employees_max'])
        company_stock_exchange.append(company_details['properties']['stock_exchange'])
        company_stock_symbol.append(company_details['properties']['stock_symbol'])
        company_total_funding_usd.append(company_details['properties']['total_funding_usd'])
        company_number_of_investments.append(company_details['properties']['number_of_investments'])
        company_homepage_url.append(company_details['properties']['homepage_url'])
        company_contact_email.append(company_details['properties']['contact_email'])
        company_phone_number.append(company_details['properties']['phone_number'])
        company_rank.append(company_details['properties']['rank'])
        company_created_at.append(company_details['properties']['created_at'])
        company_updated_at.append(company_details['properties']['updated_at'])
        
        # Owned by details for each company
        company_owned_by_paging_total_items.append(company_details['relationships']['owned_by']['paging']['total_items'])
        if company_owned_by_paging_total_items[-1]>0: #If owned by detials are available for the company, append the details
            company_owned_by_owner_type.append(company_details['relationships']['owned_by']['item']['type'])
            company_owned_by_owner_uuid.append(company_details['relationships']['owned_by']['item']['uuid'])
            company_owned_by_owner_permalink.append(company_details['relationships']['owned_by']['item']['properties']['permalink'])
            company_owned_by_owner_permalink_aliases.append(company_details['relationships']['owned_by']['item']['properties']['permalink_aliases'])
            company_owned_by_owner_api_path.append(company_details['relationships']['owned_by']['item']['properties']['api_path'])
            company_owned_by_owner_web_path.append(company_details['relationships']['owned_by']['item']['properties']['web_path'])
            company_owned_by_owner_api_url.append(company_details['relationships']['owned_by']['item']['properties']['api_url'])
            company_owned_by_owner_name.append(company_details['relationships']['owned_by']['item']['properties']['name'])
            company_owned_by_owner_also_known_as.append(company_details['relationships']['owned_by']['item']['properties']['also_known_as'])
            company_owned_by_owner_short_description.append(company_details['relationships']['owned_by']['item']['properties']['short_description'])
            company_owned_by_owner_description.append(company_details['relationships']['owned_by']['item']['properties']['description'])
            company_owned_by_owner_profile_image_url.append(company_details['relationships']['owned_by']['item']['properties']['profile_image_url'])
            company_owned_by_owner_primary_role.append(company_details['relationships']['owned_by']['item']['properties']['primary_role'])
            company_owned_by_owner_role_company.append(company_details['relationships']['owned_by']['item']['properties']['role_company'])
            company_owned_by_owner_role_investor.append(company_details['relationships']['owned_by']['item']['properties']['role_investor'])
            company_owned_by_owner_role_group.append(company_details['relationships']['owned_by']['item']['properties']['role_group'])
            company_owned_by_owner_role_school.append(company_details['relationships']['owned_by']['item']['properties']['role_school'])
            company_owned_by_owner_investor_type.append(company_details['relationships']['owned_by']['item']['properties']['investor_type'])
            company_owned_by_owner_founded_on.append(company_details['relationships']['owned_by']['item']['properties']['founded_on'])
            company_owned_by_owner_founded_on_trust_code.append(company_details['relationships']['owned_by']['item']['properties']['founded_on_trust_code'])
            company_owned_by_owner_is_closed.append(company_details['relationships']['owned_by']['item']['properties']['is_closed'])
            company_owned_by_owner_closed_on.append(company_details['relationships']['owned_by']['item']['properties']['closed_on'])
            company_owned_by_owner_closed_on_trust_code.append(company_details['relationships']['owned_by']['item']['properties']['closed_on_trust_code'])
            company_owned_by_owner_num_employees_min.append(company_details['relationships']['owned_by']['item']['properties']['num_employees_min'])
            company_owned_by_owner_num_employees_max.append(company_details['relationships']['owned_by']['item']['properties']['num_employees_max'])
            company_owned_by_owner_stock_exchange.append(company_details['relationships']['owned_by']['item']['properties']['stock_exchange'])
            company_owned_by_owner_stock_symbol.append(company_details['relationships']['owned_by']['item']['properties']['stock_symbol'])
            company_owned_by_owner_total_funding_usd.append(company_details['relationships']['owned_by']['item']['properties']['total_funding_usd'])
            company_owned_by_owner_number_of_investments.append(company_details['relationships']['owned_by']['item']['properties']['number_of_investments'])
            company_owned_by_owner_homepage_url.append(company_details['relationships']['owned_by']['item']['properties']['homepage_url'])
            company_owned_by_owner_contact_email.append(company_details['relationships']['owned_by']['item']['properties']['contact_email'])
            company_owned_by_owner_phone_number.append(company_details['relationships']['owned_by']['item']['properties']['phone_number'])
            company_owned_by_owner_rank.append(company_details['relationships']['owned_by']['item']['properties']['rank'])
            company_owned_by_owner_created_at.append(company_details['relationships']['owned_by']['item']['properties']['created_at'])
            company_owned_by_owner_updated_at.append(company_details['relationships']['owned_by']['item']['properties']['updated_at'])
            
        else: # Append as missing entries
            company_owned_by_owner_type.append('')
            company_owned_by_owner_uuid.append('')
            company_owned_by_owner_permalink.append('')
            company_owned_by_owner_permalink_aliases.append('')
            company_owned_by_owner_api_path.append('')
            company_owned_by_owner_web_path.append('')
            company_owned_by_owner_api_url.append('')
            company_owned_by_owner_name.append('')
            company_owned_by_owner_also_known_as.append('')
            company_owned_by_owner_short_description.append('')
            company_owned_by_owner_description.append('')
            company_owned_by_owner_profile_image_url.append('')
            company_owned_by_owner_primary_role.append('')
            company_owned_by_owner_role_company.append('')
            company_owned_by_owner_role_investor.append('')
            company_owned_by_owner_role_group.append('')
            company_owned_by_owner_role_school.append('')
            company_owned_by_owner_investor_type.append('')
            company_owned_by_owner_founded_on.append('')
            company_owned_by_owner_founded_on_trust_code.append('')
            company_owned_by_owner_is_closed.append('')
            company_owned_by_owner_closed_on.append('')
            company_owned_by_owner_closed_on_trust_code.append('')
            company_owned_by_owner_num_employees_min.append('')
            company_owned_by_owner_num_employees_max.append('')
            company_owned_by_owner_stock_exchange.append('')
            company_owned_by_owner_stock_symbol.append('')
            company_owned_by_owner_total_funding_usd.append('')
            company_owned_by_owner_number_of_investments.append('')
            company_owned_by_owner_homepage_url.append('')
            company_owned_by_owner_contact_email.append('')
            company_owned_by_owner_phone_number.append('')
            company_owned_by_owner_rank.append('')
            company_owned_by_owner_created_at.append('')
            company_owned_by_owner_updated_at.append('')
        
        # IPO details for each company
        ipo_paging_total_items.append(company_details['relationships']['ipo']['paging']['total_items'])
        if ipo_paging_total_items[-1]>0: # If IPO Details are available append the details
            ipo_type.append(company_details['relationships']['ipo']['item']['type'])
            ipo_uuid.append(company_details['relationships']['ipo']['item']['uuid'])
            ipo_went_public_on.append(company_details['relationships']['ipo']['item']['properties']['went_public_on'])
            ipo_stock_exchange_symbol.append(company_details['relationships']['ipo']['item']['properties']['stock_exchange_symbol'])
            ipo_stock_symbol.append(company_details['relationships']['ipo']['item']['properties']['stock_symbol'])
            ipo_shares_sold.append(company_details['relationships']['ipo']['item']['properties']['shares_sold'])
            ipo_opening_share_price.append(company_details['relationships']['ipo']['item']['properties']['opening_share_price'])
            ipo_opening_share_price_currency_code.append(company_details['relationships']['ipo']['item']['properties']['opening_share_price_currency_code'])
            ipo_opening_share_price_usd.append(company_details['relationships']['ipo']['item']['properties']['opening_share_price_usd'])
            ipo_opening_valuation.append(company_details['relationships']['ipo']['item']['properties']['opening_valuation'])
            ipo_opening_valuation_currency_code.append(company_details['relationships']['ipo']['item']['properties']['opening_valuation_currency_code'])
            ipo_opening_valuation_usd.append(company_details['relationships']['ipo']['item']['properties']['opening_valuation_usd'])
            ipo_money_raised.append(company_details['relationships']['ipo']['item']['properties']['money_raised'])
            ipo_money_raised_currency_code.append(company_details['relationships']['ipo']['item']['properties']['money_raised_currency_code'])
            ipo_money_raised_usd.append(company_details['relationships']['ipo']['item']['properties']['money_raised_usd'])
            ipo_created_at.append(company_details['relationships']['ipo']['item']['properties']['created_at'])
            ipo_updated_at.append(company_details['relationships']['ipo']['item']['properties']['updated_at'])
    
        else: # Else append as missing entries
            ipo_type.append('')
            ipo_uuid.append('')
            ipo_went_public_on.append('')
            ipo_stock_exchange_symbol.append('')
            ipo_stock_symbol.append('')
            ipo_shares_sold.append('')
            ipo_opening_share_price.append('')
            ipo_opening_share_price_currency_code.append('')
            ipo_opening_share_price_usd.append('')
            ipo_opening_valuation.append('')
            ipo_opening_valuation_currency_code.append('')
            ipo_opening_valuation_usd.append('')
            ipo_money_raised.append('')
            ipo_money_raised_currency_code.append('')
            ipo_money_raised_usd.append('')
            ipo_created_at.append('')
            ipo_updated_at.append('')
        
        # Acquired by details for each company
        acquired_by_paging_total_items.append(company_details['relationships']['acquired_by']['paging']['total_items'])
        if acquired_by_paging_total_items[-1]>0: # If Acquired By details are available append the details
            acquired_by_type.append(company_details['relationships']['acquired_by']['item']['type'])
            acquired_by_uuid.append(company_details['relationships']['acquired_by']['item']['uuid'])        
            acquired_by_api_url.append(company_details['relationships']['acquired_by']['item']['properties']['api_url'])
            acquired_by_price.append(company_details['relationships']['acquired_by']['item']['properties']['price'])
            acquired_by_price_currency_code.append(company_details['relationships']['acquired_by']['item']['properties']['price_currency_code'])
            acquired_by_price_usd.append(company_details['relationships']['acquired_by']['item']['properties']['price_usd'])
            acquired_by_payment_type.append(company_details['relationships']['acquired_by']['item']['properties']['payment_type'])
            acquired_by_acquisition_type.append(company_details['relationships']['acquired_by']['item']['properties']['acquisition_type'])
            acquired_by_acquisition_status.append(company_details['relationships']['acquired_by']['item']['properties']['acquisition_status'])
            acquired_by_disposition_of_acquired.append(company_details['relationships']['acquired_by']['item']['properties']['disposition_of_acquired'])
            acquired_by_announced_on.append(company_details['relationships']['acquired_by']['item']['properties']['announced_on'])
            acquired_by_completed_on.append(company_details['relationships']['acquired_by']['item']['properties']['completed_on'])
            acquired_by_acquirer_type.append(company_details['relationships']['acquired_by']['item']['relationships']['acquirer']['type'])
            acquired_by_acquirer_uuid.append(company_details['relationships']['acquired_by']['item']['relationships']['acquirer']['uuid'])
            acquired_by_acquirer_name.append(company_details['relationships']['acquired_by']['item']['relationships']['acquirer']['properties']['name'])
            acquired_by_acquirer_also_known_as.append(company_details['relationships']['acquired_by']['item']['relationships']['acquirer']['properties']['also_known_as'])
            acquired_by_acquirer_short_description.append(company_details['relationships']['acquired_by']['item']['relationships']['acquirer']['properties']['short_description'])
            acquired_by_acquirer_description.append(company_details['relationships']['acquired_by']['item']['relationships']['acquirer']['properties']['description'])
            acquired_by_acquirer_profile_image_url.append(company_details['relationships']['acquired_by']['item']['relationships']['acquirer']['properties']['profile_image_url'])
            acquired_by_acquirer_primary_role.append(company_details['relationships']['acquired_by']['item']['relationships']['acquirer']['properties']['primary_role'])
            acquired_by_acquirer_role_company.append(company_details['relationships']['acquired_by']['item']['relationships']['acquirer']['properties']['role_company'])
            acquired_by_acquirer_role_investor.append(company_details['relationships']['acquired_by']['item']['relationships']['acquirer']['properties']['role_investor'])
            acquired_by_acquirer_role_group.append(company_details['relationships']['acquired_by']['item']['relationships']['acquirer']['properties']['role_group'])
            acquired_by_acquirer_role_school.append(company_details['relationships']['acquired_by']['item']['relationships']['acquirer']['properties']['role_school'])
            acquired_by_acquirer_investor_type.append(company_details['relationships']['acquired_by']['item']['relationships']['acquirer']['properties']['investor_type'])
            acquired_by_acquirer_founded_on.append(company_details['relationships']['acquired_by']['item']['relationships']['acquirer']['properties']['founded_on'])
            acquired_by_acquirer_is_closed.append(company_details['relationships']['acquired_by']['item']['relationships']['acquirer']['properties']['is_closed'])
            acquired_by_acquirer_closed_on.append(company_details['relationships']['acquired_by']['item']['relationships']['acquirer']['properties']['closed_on'])
            acquired_by_acquirer_num_employees_min.append(company_details['relationships']['acquired_by']['item']['relationships']['acquirer']['properties']['num_employees_min'])
            acquired_by_acquirer_num_employees_max.append(company_details['relationships']['acquired_by']['item']['relationships']['acquirer']['properties']['num_employees_max'])
            acquired_by_acquirer_stock_exchange.append(company_details['relationships']['acquired_by']['item']['relationships']['acquirer']['properties']['stock_exchange'])
            acquired_by_acquirer_stock_symbol.append(company_details['relationships']['acquired_by']['item']['relationships']['acquirer']['properties']['stock_symbol'])
            acquired_by_acquirer_total_funding_usd.append(company_details['relationships']['acquired_by']['item']['relationships']['acquirer']['properties']['total_funding_usd'])
            acquired_by_acquirer_number_of_investments.append(company_details['relationships']['acquired_by']['item']['relationships']['acquirer']['properties']['number_of_investments'])
            acquired_by_acquirer_homepage_url.append(company_details['relationships']['acquired_by']['item']['relationships']['acquirer']['properties']['homepage_url'])
            acquired_by_acquirer_contact_email.append(company_details['relationships']['acquired_by']['item']['relationships']['acquirer']['properties']['contact_email'])
            acquired_by_acquirer_phone_number.append(company_details['relationships']['acquired_by']['item']['relationships']['acquirer']['properties']['phone_number'])
            
        else: # Else append as missing entries
            acquired_by_type.append('')
            acquired_by_uuid.append('')
            acquired_by_api_url.append('')
            acquired_by_price.append('')
            acquired_by_price_currency_code.append('')
            acquired_by_price_usd.append('')
            acquired_by_payment_type.append('')
            acquired_by_acquisition_type.append('')
            acquired_by_acquisition_status.append('')
            acquired_by_disposition_of_acquired.append('')
            acquired_by_announced_on.append('')
            acquired_by_completed_on.append('')
            acquired_by_acquirer_type.append('')
            acquired_by_acquirer_uuid.append('')
            acquired_by_acquirer_name.append('')
            acquired_by_acquirer_also_known_as.append('')
            acquired_by_acquirer_short_description.append('')
            acquired_by_acquirer_description.append('')
            acquired_by_acquirer_profile_image_url.append('')
            acquired_by_acquirer_primary_role.append('')
            acquired_by_acquirer_role_company.append('')
            acquired_by_acquirer_role_investor.append('')
            acquired_by_acquirer_role_group.append('')
            acquired_by_acquirer_role_school.append('')
            acquired_by_acquirer_investor_type.append('')
            acquired_by_acquirer_founded_on.append('')
            acquired_by_acquirer_is_closed.append('')
            acquired_by_acquirer_closed_on.append('')
            acquired_by_acquirer_num_employees_min.append('')
            acquired_by_acquirer_num_employees_max.append('')
            acquired_by_acquirer_stock_exchange.append('')
            acquired_by_acquirer_stock_symbol.append('')
            acquired_by_acquirer_total_funding_usd.append('')
            acquired_by_acquirer_number_of_investments.append('')
            acquired_by_acquirer_homepage_url.append('')
            acquired_by_acquirer_contact_email.append('')
            acquired_by_acquirer_phone_number.append('')
       
       # The following funding details for each company are scraped seperately for each funding received by the company by going to the funding url
        fundings_url = company_details['relationships']['funding_rounds']['paging']['first_page_url'] +'?user_key={}'.format(api_key)
        company_funding_url.append(fundings_url)
        try:
            response = urllib.request.urlopen(fundings_url, timeout=timeout_time_seconds)
        except:
            timeout_excep_funding_company.append(url)
            continue
        data_funding = json.loads(response.read().decode())
        funding_paging_number_of_pages= data_funding['data']['paging']['number_of_pages']
        page_fundings=1
        while page_fundings <= funding_paging_number_of_pages: # Pagination - For any item, CrunchBase API shows at most 100 entries per page. For items with over 100 entries, we have to scrape details from each page
            fundings_url = company_details['relationships']['funding_rounds']['paging']['first_page_url'] + '?page={}&sort_order=announced_on%20DESC&items_per_page=100&user_key={}'.format(page_fundings, api_key)
            
            try:
                response = urllib.request.urlopen(fundings_url,timeout=timeout_time_seconds)
            except:
                timeout_excep_fundings.append(url)
                continue
            data_fundings = json.loads(response.read().decode())
            page_fundings = page_fundings+1
            if data_fundings['data']['items'][-1]:
                for funding_details in data_fundings['data']['items']:
                    company_uuid_funding.append(company_details['uuid'])
                    company_name_funding.append(company_details['properties']['name'])
                    funding_type.append(funding_details['type'])
                    funding_uuid.append(funding_details['uuid'])
                    funding_permalink.append(funding_details['properties']['permalink'])
                    funding_api_path.append(funding_details['properties']['api_path'])
                    funding_web_path.append(funding_details['properties']['web_path'])
                    funding_api_url.append(funding_details['properties']['api_url'])
                    funding_funding_type.append(funding_details['properties']['funding_type'])
                    funding_series.append(funding_details['properties']['series'])
                    funding_series_qualifier.append(funding_details['properties']['series_qualifier'])
                    funding_announced_on.append(funding_details['properties']['announced_on'])
                    funding_announced_on_trust_code.append(funding_details['properties']['announced_on_trust_code'])
                    funding_closed_on.append(funding_details['properties']['closed_on'])
                    funding_closed_on_trust_code.append(funding_details['properties']['closed_on_trust_code'])
                    funding_funding_money_raised.append(funding_details['properties']['money_raised'])
                    funding_money_raised_currency_code.append(funding_details['properties']['money_raised_currency_code'])
                    funding_money_raised_usd.append(funding_details['properties']['money_raised_usd'])
                    funding_target_money_raised.append(funding_details['properties']['target_money_raised'])
                    funding_target_money_raised_currency_code.append(funding_details['properties']['target_money_raised_currency_code'])
                    funding_target_money_raised_usd.append(funding_details['properties']['target_money_raised_usd'])
                    funding_pre_money_valuation.append(funding_details['properties']['pre_money_valuation'])
                    funding_pre_money_valuation_currency_code.append(funding_details['properties']['pre_money_valuation_currency_code'])
                    funding_pre_money_valuation_usd.append(funding_details['properties']['pre_money_valuation_usd'])
                    funding_rank.append(funding_details['properties']['rank'])
                    funding_created_at.append(funding_details['properties']['created_at'])
                    funding_updated_at.append(funding_details['properties']['updated_at'])
                    
                    #Investor details for each funding round from each funding round url            
                    funding_url = funding_api_url[-1] + '?&user_key={}'.format(api_key)
                    
                    try:
                        response = urllib.request.urlopen(funding_url, timeout=timeout_time_seconds)
                    except:
                        timeout_excep_investors.append(url)
                        continue                
                    data_funding = json.loads(response.read().decode())
                    
                    for funding_investors in data_funding['data']['relationships']['investments']['items']:
                        # Company details for reference
                        company_uuid_funding_investor.append(company_details['uuid'])
                        company_name_funding_investor.append(company_details['properties']['name'])
                        # Funding details for reference
                        funding_type_funding_investor.append(funding_details['type'])
                        funding_uuid_funding_investor.append(funding_details['uuid'])
                        funding_permalink_funding_investor.append(funding_details['properties']['permalink'])
                        funding_api_path_funding_investor.append(funding_details['properties']['api_path'])
                        funding_web_path_funding_investor.append(funding_details['properties']['web_path'])
                        funding_api_url_funding_investor.append(funding_details['properties']['api_url'])
                        funding_funding_type_funding_investor.append(funding_details['properties']['funding_type'])
                        funding_series_funding_investor.append(funding_details['properties']['series'])
                        funding_series_qualifier_funding_investor.append(funding_details['properties']['series_qualifier'])
                        funding_announced_on_funding_investor.append(funding_details['properties']['announced_on'])
                        funding_announced_on_trust_code_funding_investor.append(funding_details['properties']['announced_on_trust_code'])
                        funding_closed_on_funding_investor.append(funding_details['properties']['closed_on'])
                        funding_closed_on_trust_code_funding_investor.append(funding_details['properties']['closed_on_trust_code'])
                        funding_funding_money_raised_funding_investor.append(funding_details['properties']['money_raised'])
                        funding_money_raised_currency_code_funding_investor.append(funding_details['properties']['money_raised_currency_code'])
                        funding_money_raised_usd_funding_investor.append(funding_details['properties']['money_raised_usd'])
                        funding_target_money_raised_funding_investor.append(funding_details['properties']['target_money_raised'])
                        funding_target_money_raised_currency_code_funding_investor.append(funding_details['properties']['target_money_raised_currency_code'])
                        funding_target_money_raised_usd_funding_investor.append(funding_details['properties']['target_money_raised_usd'])
                        funding_pre_money_valuation_funding_investor.append(funding_details['properties']['pre_money_valuation'])
                        funding_pre_money_valuation_currency_code_funding_investor.append(funding_details['properties']['pre_money_valuation_currency_code'])
                        funding_pre_money_valuation_usd_funding_investor.append(funding_details['properties']['pre_money_valuation_usd'])
                        funding_rank_funding_investor.append(funding_details['properties']['rank'])
                        funding_created_at_funding_investor.append(funding_details['properties']['created_at'])
                        funding_updated_at_funding_investor.append(funding_details['properties']['updated_at'])
                        # Investor details
                        funding_investor_money_invested.append(funding_investors['properties']['money_invested'])
                        funding_investor_money_invested_currency_code.append(funding_investors['properties']['money_invested_currency_code'])
                        funding_investor_money_invested_usd.append(funding_investors['properties']['money_invested_usd'])
                        funding_investor_is_lead_investor.append(funding_investors['properties']['is_lead_investor'])
                        funding_investor_type.append(funding_investors['relationships']['investors']['type'])
                        funding_investor_uuid.append(funding_investors['relationships']['investors']['uuid'])
                        funding_investor_permalink.append(funding_investors['relationships']['investors']['properties']['permalink'])
                        funding_investor_permalink_aliases.append(funding_investors['relationships']['investors']['properties']['permalink_aliases'])
                        funding_investor_api_path.append(funding_investors['relationships']['investors']['properties']['api_path'])
                        funding_investor_web_path.append(funding_investors['relationships']['investors']['properties']['web_path'])
                        funding_investor_api_url.append(funding_investors['relationships']['investors']['properties']['api_url'])
                        funding_investor_rank.append(funding_investors['relationships']['investors']['properties']['rank'])
                        funding_investor_created_at.append(funding_investors['relationships']['investors']['properties']['created_at'])
                        funding_investor_updated_at.append(funding_investors['relationships']['investors']['properties']['updated_at'])
                        funding_investor_profile_image_url.append(funding_investors['relationships']['investors']['properties']['profile_image_url'])
                        
                        if funding_investor_type[-1] == 'Organization': #Different details depending upon whether the investor is organization or person             
                            funding_investor_name.append(funding_investors['relationships']['investors']['properties']['name'])
                            funding_investor_also_known_as.append(funding_investors['relationships']['investors']['properties']['also_known_as'])
                            funding_investor_short_description.append(funding_investors['relationships']['investors']['properties']['short_description'])
                            funding_investor_description.append(funding_investors['relationships']['investors']['properties']['description'])
                            funding_investor_primary_role.append(funding_investors['relationships']['investors']['properties']['primary_role'])
                            funding_investor_role_company.append(funding_investors['relationships']['investors']['properties']['role_company'])
                            funding_investor_role_investor.append(funding_investors['relationships']['investors']['properties']['role_investor'])
                            funding_investor_role_group.append(funding_investors['relationships']['investors']['properties']['role_group'])
                            funding_investor_role_school.append(funding_investors['relationships']['investors']['properties']['role_school'])
                            funding_investor_investor_type.append(funding_investors['relationships']['investors']['properties']['investor_type'])
                            funding_investor_founded_on.append(funding_investors['relationships']['investors']['properties']['founded_on'])
                            funding_investor_founded_on_trust_code.append(funding_investors['relationships']['investors']['properties']['founded_on_trust_code'])
                            funding_investor_is_closed.append(funding_investors['relationships']['investors']['properties']['is_closed'])
                            funding_investor_closed_on.append(funding_investors['relationships']['investors']['properties']['closed_on'])
                            funding_investor_closed_on_trust_code.append(funding_investors['relationships']['investors']['properties']['closed_on_trust_code'])
                            funding_investor_num_employees_min.append(funding_investors['relationships']['investors']['properties']['num_employees_min'])
                            funding_investor_num_employees_max.append(funding_investors['relationships']['investors']['properties']['num_employees_max'])
                            funding_investor_stock_exchange.append(funding_investors['relationships']['investors']['properties']['stock_exchange'])
                            funding_investor_stock_symbol.append(funding_investors['relationships']['investors']['properties']['stock_symbol'])
                            funding_investor_total_funding_usd.append(funding_investors['relationships']['investors']['properties']['total_funding_usd'])
                            funding_investor_number_of_investments.append(funding_investors['relationships']['investors']['properties']['number_of_investments'])
                            funding_investor_homepage_url.append(funding_investors['relationships']['investors']['properties']['homepage_url'])
                            funding_investor_contact_email.append(funding_investors['relationships']['investors']['properties']['contact_email'])
                            funding_investor_phone_number.append(funding_investors['relationships']['investors']['properties']['phone_number'])
                            funding_investor_first_name.append('')
                            funding_investor_last_name.append('')
                            funding_investor_gender.append('')
                            funding_investor_bio.append('')
                            funding_investor_born_on.append('')
                            funding_investor_born_on_trust_code.append('')
                            funding_investor_died_on.append('')
                            funding_investor_died_on_trust_code.append('')
                            
                        else: #Different details depending upon whether the investor is organization or person
                            funding_investor_name.append('')
                            funding_investor_also_known_as.append('')
                            funding_investor_short_description.append('')
                            funding_investor_description.append('')
                            funding_investor_primary_role.append('')
                            funding_investor_role_company.append('')
                            funding_investor_role_investor.append('')
                            funding_investor_role_group.append('')
                            funding_investor_role_school.append('')
                            funding_investor_investor_type.append('')
                            funding_investor_founded_on.append('')
                            funding_investor_founded_on_trust_code.append('')
                            funding_investor_is_closed.append('')
                            funding_investor_closed_on.append('')
                            funding_investor_closed_on_trust_code.append('')
                            funding_investor_num_employees_min.append('')
                            funding_investor_num_employees_max.append('')
                            funding_investor_stock_exchange.append('')
                            funding_investor_stock_symbol.append('')
                            funding_investor_total_funding_usd.append('')
                            funding_investor_number_of_investments.append('')
                            funding_investor_homepage_url.append('')
                            funding_investor_contact_email.append('')
                            funding_investor_phone_number.append('')
                            funding_investor_first_name.append(funding_investors['relationships']['investors']['properties']['first_name'])
                            funding_investor_last_name.append(funding_investors['relationships']['investors']['properties']['last_name'])
                            funding_investor_gender.append(funding_investors['relationships']['investors']['properties']['gender'])
                            funding_investor_bio.append(funding_investors['relationships']['investors']['properties']['bio'])
                            funding_investor_born_on.append(funding_investors['relationships']['investors']['properties']['born_on'])
                            funding_investor_born_on_trust_code.append(funding_investors['relationships']['investors']['properties']['born_on_trust_code'])
                            funding_investor_died_on.append(funding_investors['relationships']['investors']['properties']['died_on'])
                            funding_investor_died_on_trust_code.append(funding_investors['relationships']['investors']['properties']['died_on_trust_code'])
                        
                        for funding_investors_items in data_funding['data']['relationships']['investments']['items']:
                            for funding_investors_partners in funding_investors_items['relationships']['partners']:
                                company_uuid_funding_investor_partner.append(company_details['uuid'])
                                company_name_funding_investor_partner.append(company_details['properties']['name'])
                                funding_type_funding_investor_partner.append(funding_details['type'])
                                funding_uuid_funding_investor_partner.append(funding_details['uuid'])
                                funding_funding_type_funding_investor_partner.append(funding_details['properties']['funding_type'])
                                funding_series_funding_investor_partner.append(funding_details['properties']['series'])
                                funding_announced_on_funding_investor_partner.append(funding_details['properties']['announced_on'])
                                funding_investor_uuid_investor_partner.append(funding_investors['relationships']['investors']['uuid'])                
                                funding_investor_partner_type.append(funding_investors_partners['type'])
                                funding_investor_partner_uuid.append(funding_investors_partners['uuid'])
                                funding_investor_partner_permalink.append(funding_investors_partners['properties']['permalink'])
                                funding_investor_partner_permalink_aliases.append(funding_investors_partners['properties']['permalink_aliases'])
                                funding_investor_partner_api_path.append(funding_investors_partners['properties']['api_path'])
                                funding_investor_partner_web_path.append(funding_investors_partners['properties']['web_path'])
                                funding_investor_partner_api_url.append(funding_investors_partners['properties']['api_url'])
                                funding_investor_partner_first_name.append(funding_investors_partners['properties']['first_name'])
                                funding_investor_partner_last_name.append(funding_investors_partners['properties']['last_name'])
                                funding_investor_partner_gender.append(funding_investors_partners['properties']['gender'])
                                funding_investor_partner_also_known_as.append(funding_investors_partners['properties']['also_known_as'])
                                funding_investor_partner_bio.append(funding_investors_partners['properties']['bio'])
                                funding_investor_partner_profile_image_url.append(funding_investors_partners['properties']['profile_image_url'])
                                funding_investor_partner_role_investor.append(funding_investors_partners['properties']['role_investor'])
                                funding_investor_partner_born_on.append(funding_investors_partners['properties']['born_on'])
                                funding_investor_partner_born_on_trust_code.append(funding_investors_partners['properties']['born_on_trust_code'])
                                funding_investor_partner_died_on.append(funding_investors_partners['properties']['died_on'])
                                funding_investor_partner_died_on_trust_code.append(funding_investors_partners['properties']['died_on_trust_code'])
                                funding_investor_partner_rank.append(funding_investors_partners['properties']['rank'])
                                funding_investor_partner_created_at.append(funding_investors_partners['properties']['created_at'])
                                funding_investor_partner_updated_at.append(funding_investors_partners['properties']['updated_at'])   
            else:
                company_uuid_funding.append('')
                company_name_funding.append('')
                funding_type.append('')
                funding_uuid.append('')
                funding_permalink.append('')
                funding_api_path.append('')
                funding_web_path.append('')
                funding_api_url.append('')
                funding_funding_type.append('')
                funding_series.append('')
                funding_series_qualifier.append('')
                funding_announced_on.append('')
                funding_announced_on_trust_code.append('')
                funding_closed_on.append('')
                funding_closed_on_trust_code.append('')
                funding_funding_money_raised.append('')
                funding_money_raised_currency_code.append('')
                funding_money_raised_usd.append('')
                funding_target_money_raised.append('')
                funding_target_money_raised_currency_code.append('')
                funding_target_money_raised_usd.append('')
                funding_pre_money_valuation.append('')
                funding_pre_money_valuation_currency_code.append('')
                funding_pre_money_valuation_usd.append('')
                funding_rank.append('')
                funding_created_at.append('')
                funding_updated_at.append('')
                company_uuid_funding_investor.append('')
                company_name_funding_investor.append('')
                # Funding details for reference
                funding_type_funding_investor.append('')
                funding_uuid_funding_investor.append('')
                funding_permalink_funding_investor.append('')
                funding_api_path_funding_investor.append('')
                funding_web_path_funding_investor.append('')
                funding_api_url_funding_investor.append('')
                funding_funding_type_funding_investor.append('')
                funding_series_funding_investor.append('')
                funding_series_qualifier_funding_investor.append('')
                funding_announced_on_funding_investor.append('')
                funding_announced_on_trust_code_funding_investor.append('')
                funding_closed_on_funding_investor.append('')
                funding_closed_on_trust_code_funding_investor.append('')
                funding_funding_money_raised_funding_investor.append('')
                funding_money_raised_currency_code_funding_investor.append('')
                funding_money_raised_usd_funding_investor.append('')
                funding_target_money_raised_funding_investor.append('')
                funding_target_money_raised_currency_code_funding_investor.append('')
                funding_target_money_raised_usd_funding_investor.append('')
                funding_pre_money_valuation_funding_investor.append('')
                funding_pre_money_valuation_currency_code_funding_investor.append('')
                funding_pre_money_valuation_usd_funding_investor.append('')
                funding_rank_funding_investor.append('')
                funding_created_at_funding_investor.append('')
                funding_updated_at_funding_investor.append('')
                # Investor details
                funding_investor_money_invested.append('')
                funding_investor_money_invested_currency_code.append('')
                funding_investor_money_invested_usd.append('')
                funding_investor_is_lead_investor.append('')
                funding_investor_type.append('')
                funding_investor_uuid.append('')
                funding_investor_permalink.append('')
                funding_investor_permalink_aliases.append('')
                funding_investor_api_path.append('')
                funding_investor_web_path.append('')
                funding_investor_api_url.append('')
                funding_investor_rank.append('')
                funding_investor_created_at.append('')
                funding_investor_updated_at.append('')
                funding_investor_profile_image_url.append('')
                funding_investor_name.append('')
                funding_investor_also_known_as.append('')
                funding_investor_short_description.append('')
                funding_investor_description.append('')
                funding_investor_primary_role.append('')
                funding_investor_role_company.append('')
                funding_investor_role_investor.append('')
                funding_investor_role_group.append('')
                funding_investor_role_school.append('')
                funding_investor_investor_type.append('')
                funding_investor_founded_on.append('')
                funding_investor_founded_on_trust_code.append('')
                funding_investor_is_closed.append('')
                funding_investor_closed_on.append('')
                funding_investor_closed_on_trust_code.append('')
                funding_investor_num_employees_min.append('')
                funding_investor_num_employees_max.append('')
                funding_investor_stock_exchange.append('')
                funding_investor_stock_symbol.append('')
                funding_investor_total_funding_usd.append('')
                funding_investor_number_of_investments.append('')
                funding_investor_homepage_url.append('')
                funding_investor_contact_email.append('')
                funding_investor_phone_number.append('')
                funding_investor_first_name.append('')
                funding_investor_last_name.append('')
                funding_investor_gender.append('')
                funding_investor_bio.append('')
                funding_investor_born_on.append('')
                funding_investor_born_on_trust_code.append('')
                funding_investor_died_on.append('')
                funding_investor_died_on_trust_code.append('')
                company_uuid_funding_investor_partner.append('')
                company_name_funding_investor_partner.append('')
                funding_type_funding_investor_partner.append('')
                funding_uuid_funding_investor_partner.append('')
                funding_funding_type_funding_investor_partner.append('')
                funding_series_funding_investor_partner.append('')
                funding_announced_on_funding_investor_partner.append('')
                funding_investor_uuid_investor_partner.append('')                
                funding_investor_partner_type.append('')
                funding_investor_partner_uuid.append('')
                funding_investor_partner_permalink.append('')
                funding_investor_partner_permalink_aliases.append('')
                funding_investor_partner_api_path.append('')
                funding_investor_partner_web_path.append('')
                funding_investor_partner_api_url.append('')
                funding_investor_partner_first_name.append('')
                funding_investor_partner_last_name.append('')
                funding_investor_partner_gender.append('')
                funding_investor_partner_also_known_as.append('')
                funding_investor_partner_bio.append('')
                funding_investor_partner_profile_image_url.append('')
                funding_investor_partner_role_investor.append('')
                funding_investor_partner_born_on.append('')
                funding_investor_partner_born_on_trust_code.append('')
                funding_investor_partner_died_on.append('')
                funding_investor_partner_died_on_trust_code.append('')
                funding_investor_partner_rank.append('')
                funding_investor_partner_created_at.append('')
                funding_investor_partner_updated_at.append('')                                
        # The following acquisition details for each company are scraped seperately for each acquisition done by the company by going to the acquisitions url
        acquisition_url = company_details['relationships']['acquisitions']['paging']\
        ['first_page_url'] +'?user_key={}'.format(api_key)
        company_acquisition_url.append(acquisition_url)
        
        try:
            response = urllib.request.urlopen(acquisition_url, timeout=timeout_time_seconds)
        except:
            timeout_exceptions_acquistions.append(url)
        
        data_acquisition = json.loads(response.read().decode())
        acquisition_paging_number_of_pages= data_acquisition['data']['paging']['number_of_pages']
        page=1
        while page <= acquisition_paging_number_of_pages: # Pagination - For any item, CrunchBase API shows at most 100 entries per page. For items with over 100 entries, we have to scrape details from each page
            acquisition_url = company_details['relationships']['acquisitions']['paging']['first_page_url'] + '?page={}&sort_order=announced_on__value%20DESC&items_per_page=100&user_key={}'.format(page, api_key)
            
            try:
                response = urllib.request.urlopen(acquisition_url, timeout=timeout_time_seconds)
            except:
                timeout_except_acquisition.append(url)
                continue
            data_acquisition = json.loads(response.read().decode())
            page = page+1
            for acquisition_details in data_acquisition['data']['items']:
                company_uuid_acquisition.append(company_details['uuid'])
                company_name_acquisition.append(company_details['properties']['name'])
                acquisition_type.append(acquisition_details['type'])
                acquisition_uuid.append(acquisition_details['uuid'])
                acquisition_permalink.append(acquisition_details['properties']['permalink'])
                acquisition_api_path.append(acquisition_details['properties']['api_path'])
                acquisition_web_path.append(acquisition_details['properties']['web_path'])
                acquisition_api_url.append(acquisition_details['properties']['api_url'])
                acquisition_price.append(acquisition_details['properties']['price'])
                acquisition_price_currency_code.append(acquisition_details['properties']['price_currency_code'])
                acquisition_price_usd.append(acquisition_details['properties']['price_usd'])
                acquisition_payment_type.append(acquisition_details['properties']['payment_type'])
                acquisition_acquisition_type.append(acquisition_details['properties']['acquisition_type'])
                acquisition_acquisition_status.append(acquisition_details['properties']['acquisition_status'])
                acquisition_disposition_of_acquired.append(acquisition_details['properties']['disposition_of_acquired'])
                acquisition_announced_on.append(acquisition_details['properties']['announced_on'])
                acquisition_announced_on_trust_code.append(acquisition_details['properties']['announced_on_trust_code'])
                acquisition_completed_on.append(acquisition_details['properties']['completed_on'])
                acquisition_completed_on_trust_code.append(acquisition_details['properties']['completed_on_trust_code'])
                acquisition_rank.append(acquisition_details['properties']['rank'])            
                acquisition_created_at.append(acquisition_details['properties']['created_at'])
                acquisition_updated_at.append(acquisition_details['properties']['updated_at'])
                target_type.append(acquisition_details['relationships']['acquiree']['type'])
                target_uuid.append(acquisition_details['relationships']['acquiree']['uuid'])
                target_permalink.append(acquisition_details['relationships']['acquiree']['properties']['permalink'])
                target_permalink_aliases.append(acquisition_details['relationships']['acquiree']['properties']['permalink_aliases'])
                target_api_path.append(acquisition_details['relationships']['acquiree']['properties']['api_path'])
                target_web_path.append(acquisition_details['relationships']['acquiree']['properties']['web_path'])
                target_api_url.append(acquisition_details['relationships']['acquiree']['properties']['api_url'])
                target_name.append(acquisition_details['relationships']['acquiree']['properties']['name'])
                target_also_known_as.append(acquisition_details['relationships']['acquiree']['properties']['also_known_as'])
                target_short_description.append(acquisition_details['relationships']['acquiree']['properties']['short_description'])
                target_description.append(acquisition_details['relationships']['acquiree']['properties']['description'])
                target_profile_image_url.append(acquisition_details['relationships']['acquiree']['properties']['profile_image_url'])
                target_primary_role.append(acquisition_details['relationships']['acquiree']['properties']['primary_role'])
                target_role_company.append(acquisition_details['relationships']['acquiree']['properties']['role_company'])
                target_role_investor.append(acquisition_details['relationships']['acquiree']['properties']['role_investor'])
                target_role_group.append(acquisition_details['relationships']['acquiree']['properties']['role_group'])
                target_role_school.append(acquisition_details['relationships']['acquiree']['properties']['role_school'])
                target_investor_type.append(acquisition_details['relationships']['acquiree']['properties']['investor_type'])
                target_founded_on.append(acquisition_details['relationships']['acquiree']['properties']['founded_on'])
                target_founded_on_trust_code.append(acquisition_details['relationships']['acquiree']['properties']['founded_on_trust_code'])
                target_is_closed.append(acquisition_details['relationships']['acquiree']['properties']['is_closed'])
                target_closed_on.append(acquisition_details['relationships']['acquiree']['properties']['closed_on'])
                target_closed_on_trust_code.append(acquisition_details['relationships']['acquiree']['properties']['closed_on_trust_code'])
                target_num_employees_min.append(acquisition_details['relationships']['acquiree']['properties']['num_employees_min'])
                target_num_employees_max.append(acquisition_details['relationships']['acquiree']['properties']['num_employees_max'])
                target_stock_exchange.append(acquisition_details['relationships']['acquiree']['properties']['stock_exchange'])
                target_stock_symbol.append(acquisition_details['relationships']['acquiree']['properties']['stock_symbol'])
                target_total_funding_usd.append(acquisition_details['relationships']['acquiree']['properties']['total_funding_usd'])
                target_number_of_investments.append(acquisition_details['relationships']['acquiree']['properties']['number_of_investments'])
                target_homepage_url.append(acquisition_details['relationships']['acquiree']['properties']['homepage_url'])
                target_contact_email.append(acquisition_details['relationships']['acquiree']['properties']['contact_email'])
                target_phone_number.append(acquisition_details['relationships']['acquiree']['properties']['phone_number'])
                target_rank.append(acquisition_details['relationships']['acquiree']['properties']['rank'])
                target_created_at.append(acquisition_details['relationships']['acquiree']['properties']['created_at'])
                target_updated_at.append(acquisition_details['relationships']['acquiree']['properties']['updated_at'])
        
        # The following office details for each company are scraped seperately for each company by going to the offices url
            offices_url = company_details['relationships']['offices']['paging']['first_page_url'] +'?user_key={}'.format(api_key)
            
            try:
                response = urllib.request.urlopen(offices_url, timeout=timeout_time_seconds)
            except:
                timeout_except_offices.append(url)
                continue
            data_offices = json.loads(response.read().decode())
            company_offices_paging_number_of_pages= data_offices['data']['paging']['number_of_pages']
            page_offices=1
            while page_offices <= company_offices_paging_number_of_pages: # Pagination - For any item, CrunchBase API shows at most 100 entries per page. For items with over 100 entries, we have to scrape details from each page
                offices_url = company_details['relationships']['offices']['paging']['first_page_url'] + '?page={}items_per_page=100&user_key={}'.format(page_offices, api_key)
                
                try:
                    response = urllib.request.urlopen(offices_url, timeout=timeout_time_seconds)
                except:
                    timeout_except_office.append(url)
                    continue
                data_offices = json.loads(response.read().decode())
                page_offices = page_offices+1
                for company_offices in data_offices['data']['items']:
                    company_offices_total_items.append(data_offices['data']['paging']['total_items'])
                    if company_offices_total_items[-1]>0:
                        company_uuid_offices.append(company_details['uuid'])
                        company_name_offices.append(company_details['properties']['name'])
                        company_office_type.append(company_offices['type'])
                        company_office_uuid.append(company_offices['uuid'])
                        company_office_street_1.append(company_offices['properties']['street_1'])
                        company_office_street_2.append(company_offices['properties']['street_2'])
                        company_office_postal_code.append(company_offices['properties']['postal_code'])
                        company_office_city.append(company_offices['properties']['city'])
                        company_office_region.append(company_offices['properties']['region'])
                        company_office_country.append(company_offices['properties']['country'])
                        company_office_city_web_path.append(company_offices['properties']['city_web_path'])
                        company_office_region_code2.append(company_offices['properties']['region_code2'])
                        company_office_region_web_path.append(company_offices['properties']['region_web_path'])
                        company_office_country_code2.append(company_offices['properties']['country_code2'])
                        company_office_country_code3.append(company_offices['properties']['country_code3'])
                        company_office_country_web_path.append(company_offices['properties']['latitude'])
                        company_office_latitude.append(company_offices['properties']['street_2'])
                        company_office_longitude.append(company_offices['properties']['longitude'])
                        company_office_created_at.append(company_offices['properties']['created_at'])
                        company_office_updated_at.append(company_offices['properties']['updated_at'])
                    else:
                        company_uuid_offices.append('')
                        company_name_offices.append('')
                        company_office_type.append('')
                        company_office_uuid.append('')
                        company_office_street_1.append('')
                        company_office_street_2.append('')
                        company_office_postal_code.append('')
                        company_office_city.append('')
                        company_office_region.append('')
                        company_office_country.append('')
                        company_office_city_web_path.append('')
                        company_office_region_code2.append('')
                        company_office_region_web_path.append('')
                        company_office_country_code2.append('')
                        company_office_country_code3.append('')
                        company_office_country_web_path.append('')
                        company_office_latitude.append('')
                        company_office_longitude.append('')
                        company_office_created_at.append('')
                        company_office_updated_at.append('')
                                    
        # The following headquarters details for each company are scraped seperately for each company by going to the headquarters url
        headquarters_url = company_details['relationships']['headquarters']['paging']['first_page_url'] +'?user_key={}'.format(api_key)
        
        try:
            response = urllib.request.urlopen(headquarters_url, timeout=timeout_time_seconds)
        except:
            timeout_excep_headquarters.append(url)
            continue
        data_headquarters = json.loads(response.read().decode())
        company_headquarters_paging_number_of_pages= data_headquarters['data']['paging']['number_of_pages']
        page_headquarters=1
        while page_headquarters <= company_headquarters_paging_number_of_pages: # Pagination - For any item, CrunchBase API shows at most 100 entries per page. For items with over 100 entries, we have to scrape details from each page
            headquarters_url = company_details['relationships']['headquarters']['paging']['first_page_url'] + '?page={}items_per_page=100&user_key={}'.format(page_headquarters, api_key)
            
            try:
                response = urllib.request.urlopen(headquarters_url, timeout=timeout_time_seconds)
            except:
                timeout_excep_headquarter.append(url)
                continue
            response = urllib.request.urlopen(headquarters_url)
            data_headquarters = json.loads(response.read().decode())
            page_headquarters = page_headquarters+1
            for company_headquarters in data_headquarters['data']['items']:
                company_headquarters_total_items.append(data_headquarters['data']['paging']['total_items'])
                if company_headquarters_total_items[-1]>0: # If Company headquarters details are available, append the details
                    company_uuid_headquarters.append(company_details['uuid'])
                    company_name_headquarters.append(company_details['properties']['name'])
                    company_headquarters_type.append(company_headquarters['type'])
                    company_headquarters_uuid.append(company_headquarters['uuid'])
                    company_headquarters_name.append(company_headquarters['properties']['name'])
                    company_headquarters_street_1.append(company_headquarters['properties']['street_1'])
                    company_headquarters_street_2.append(company_headquarters['properties']['street_2'])
                    company_headquarters_postal_code.append(company_headquarters['properties']['postal_code'])
                    company_headquarters_city.append(company_headquarters['properties']['city'])
                    company_headquarters_region.append(company_headquarters['properties']['region'])
                    company_headquarters_country.append(company_headquarters['properties']['country'])
                    company_headquarters_city_web_path.append(company_headquarters['properties']['city_web_path'])
                    company_headquarters_region_code2.append(company_headquarters['properties']['region_code2'])
                    company_headquarters_region_web_path.append(company_headquarters['properties']['region_web_path'])
                    company_headquarters_country_code2.append(company_headquarters['properties']['country_code2'])
                    company_headquarters_country_code3.append(company_headquarters['properties']['country_code3'])
                    company_headquarters_country_web_path.append(company_headquarters['properties']['latitude'])
                    company_headquarters_latitude.append(company_headquarters['properties']['street_2'])
                    company_headquarters_longitude.append(company_headquarters['properties']['longitude'])
                    company_headquarters_created_at.append(company_headquarters['properties']['created_at'])
                    company_headquarters_updated_at.append(company_headquarters['properties']['updated_at'])
                else: #Else, append as missing entries
                    company_uuid_headquarters.append(company_details['uuid'])
                    company_name_headquarters.append(company_details['properties']['name'])
                    company_headquarters_type.append('')
                    company_headquarters_uuid.append('')
                    company_headquarters_name.append('')
                    company_headquarters_street_1.append('')
                    company_headquarters_street_2.append('')
                    company_headquarters_postal_code.append('')
                    company_headquarters_city.append('')
                    company_headquarters_region.append('')
                    company_headquarters_country.append('')
                    company_headquarters_city_web_path.append('')
                    company_headquarters_region_code2.append('')
                    company_headquarters_region_web_path.append('')
                    company_headquarters_country_code2.append('')
                    company_headquarters_country_code3.append('')
                    company_headquarters_country_web_path.append('')
                    company_headquarters_latitude.append('')
                    company_headquarters_longitude.append('')
                    company_headquarters_created_at.append('')
                    company_headquarters_updated_at.append('')
                    
        # The following details are scraped for all sub-organizations of the company by going to the sub_organizations url
        sub_organizations_url = company_details['relationships']['sub_organizations']['paging']['first_page_url'] +'?user_key={}'.format(api_key)
        company_sub_organizations_url.append(sub_organizations_url)
        
        try:
            response = urllib.request.urlopen(sub_organizations_url, timeout=timeout_time_seconds)
        except:
            time_excep_suborganisations.append(url)
            continue
        data_sub_organizations = json.loads(response.read().decode())
        sub_organizations_paging_number_of_pages= data_sub_organizations['data']['paging']['number_of_pages']
        page_sub_organizations=1
        while page_sub_organizations <= sub_organizations_paging_number_of_pages: # Pagination - For any item, CrunchBase API shows at most 100 entries per page. For items with over 100 entries, we have to scrape details from each page
            sub_organizations_url = company_details['relationships']['sub_organizations']['paging']['first_page_url'] + '?page={}%20DESC&items_per_page=100&user_key={}'.format(page_sub_organizations, api_key)
            
            try:
                response = urllib.request.urlopen(sub_organizations_url, timeout=timeout_time_seconds)
            except:
                time_excep_suborganisation.append(url)
                continue
            data_sub_organizations = json.loads(response.read().decode())
            page_sub_organizations = page_sub_organizations+1
            for sub_organizations_details in data_sub_organizations['data']['items']:
                company_uuid_sub_organizations.append(company_details['uuid'])
                company_name_sub_organizations.append(company_details['properties']['name'])
                sub_organization_type.append(sub_organizations_details['type'])
                sub_organization_uuid.append(sub_organizations_details['uuid'])    
                sub_organization_permalink.append(sub_organizations_details['properties']['permalink'])
                sub_organization_permalink_aliases.append(sub_organizations_details['properties']['permalink_aliases'])
                sub_organization_api_path.append(sub_organizations_details['properties']['api_path'])
                sub_organization_web_path.append(sub_organizations_details['properties']['web_path'])
                sub_organization_api_url.append(sub_organizations_details['properties']['api_url'])
                sub_organization_name.append(sub_organizations_details['properties']['name'])
                sub_organization_also_known_as.append(sub_organizations_details['properties']['also_known_as'])
                sub_organization_short_description.append(sub_organizations_details['properties']['short_description'])
                sub_organization_description.append(sub_organizations_details['properties']['description'])
                sub_organization_profile_image_url.append(sub_organizations_details['properties']['profile_image_url'])
                sub_organization_primary_role.append(sub_organizations_details['properties']['primary_role'])
                sub_organization_role_company.append(sub_organizations_details['properties']['role_company'])
                sub_organization_role_investor.append(sub_organizations_details['properties']['role_investor'])
                sub_organization_role_group.append(sub_organizations_details['properties']['role_group'])
                sub_organization_role_school.append(sub_organizations_details['properties']['role_school'])
                sub_organization_investor_type.append(sub_organizations_details['properties']['investor_type'])
                sub_organization_founded_on.append(sub_organizations_details['properties']['founded_on'])
                sub_organization_founded_on_trust_code.append(sub_organizations_details['properties']['founded_on_trust_code'])
                sub_organization_is_closed.append(sub_organizations_details['properties']['is_closed'])
                sub_organization_closed_on.append(sub_organizations_details['properties']['closed_on'])
                sub_organization_closed_on_trust_code.append(sub_organizations_details['properties']['closed_on_trust_code'])
                sub_organization_num_employees_min.append(sub_organizations_details['properties']['num_employees_min'])
                sub_organization_num_employees_max.append(sub_organizations_details['properties']['num_employees_max'])
                sub_organization_stock_exchange.append(sub_organizations_details['properties']['stock_exchange'])
                sub_organization_stock_symbol.append(sub_organizations_details['properties']['stock_symbol'])
                sub_organization_total_funding_usd.append(sub_organizations_details['properties']['total_funding_usd'])
                sub_organization_number_of_investments.append(sub_organizations_details['properties']['number_of_investments'])
                sub_organization_homepage_url.append(sub_organizations_details['properties']['homepage_url'])
                sub_organization_contact_email.append(sub_organizations_details['properties']['contact_email'])
                sub_organization_phone_number.append(sub_organizations_details['properties']['phone_number'])
                sub_organization_rank.append(sub_organizations_details['properties']['rank'])
                sub_organization_created_at.append(sub_organizations_details['properties']['created_at'])
                sub_organization_updated_at.append(sub_organizations_details['properties']['updated_at'])
        
        # The following details are scraped for all founders of the company by going to the founders url
        founders_url = company_details['relationships']['founders']['paging']\
        ['first_page_url'] +'?user_key={}'.format(api_key)
        company_founders_url.append(founders_url)
        
        try:
            response = urllib.request.urlopen(founders_url, timeout=timeout_time_seconds)
        except:
            time_excep_company_founders.append(url)
            continue
        data_founders = json.loads(response.read().decode())
        founder_paging_number_of_pages= data_founders['data']['paging']['number_of_pages']
        page_founders=1
        while page_founders <= founder_paging_number_of_pages: # Pagination - For any item, CrunchBase API shows at most 100 entries per page. For items with over 100 entries, we have to scrape details from each page
            founders_url = company_details['relationships']['founders']['paging']['first_page_url'] + '?page={}%20DESC&items_per_page=100&user_key={}'.format(page_founders, api_key)
            
            try:
                response = urllib.request.urlopen(founders_url, timeout=timeout_time_seconds)
            except:
                time_excep_company_founder.append(url)
                continue
            data_founders = json.loads(response.read().decode())
            page_founders = page_founders+1
            for founders_details in data_founders['data']['items']:
                company_uuid_founder.append(company_details['uuid'])
                company_name_founder.append(company_details['properties']['name'])
                founder_type.append(founders_details['type'])
                founder_uuid.append(founders_details['uuid'])
                founder_permalink.append(founders_details['properties']['permalink'])
                founder_api_path.append(founders_details['properties']['api_path'])
                founder_web_path.append(founders_details['properties']['web_path'])
                founder_api_url.append(founders_details['properties']['api_url'])
                founder_first_name.append(founders_details['properties']['first_name'])
                founder_last_name.append(founders_details['properties']['last_name'])
                founder_gender.append(founders_details['properties']['gender'])
                founder_also_known_as.append(founders_details['properties']['also_known_as'])
                founder_bio.append(founders_details['properties']['bio'])
                founder_profile_image_url.append(founders_details['properties']['profile_image_url'])
                founder_role_investor.append(founders_details['properties']['role_investor'])
                founder_born_on.append(founders_details['properties']['born_on'])
                founder_born_on_trust_code.append(founders_details['properties']['born_on_trust_code'])
                founder_died_on.append(founders_details['properties']['died_on'])
                founder_died_on_trust_code.append(founders_details['properties']['died_on_trust_code'])
                founder_rank.append(founders_details['properties']['rank'])
                founder_created_at.append(founders_details['properties']['created_at'])
                founder_updated_at.append(founders_details['properties']['updated_at'])
                
                # The following details are scraped for each founder of the company by going to the individual founder's url
                founder_url= 'https://api.crunchbase.com/v3.1/people/{}?user_key={}'.format(founders_details['uuid'], api_key)
                
                try:
                    response = urllib.request.urlopen(founder_url, timeout=timeout_time_seconds)
                except:
                    timeout_excep_founder_details.append(url)
                    continue
                data_founder = json.loads(response.read().decode())
                founder_details = data_founder['data']['relationships']
                # Primary locations for each founder
                founder_primary_location_total_items.append(founder_details['primary_location']['paging']['total_items'])
                if founder_primary_location_total_items[-1] >0: # If founder location details are available, append the details
                    founder_primary_location_type.append(founder_details['primary_location']['item']['type'])
                    founder_primary_location_uuid.append(founder_details['primary_location']['item']['uuid'])
                    founder_primary_location_location_type.append(founder_details['primary_location']['item']['properties']['location_type'])
                    founder_primary_location_parent_location_uuid.append(founder_details['primary_location']['item']['properties']['parent_location_uuid'])
                    founder_primary_location_city.append(founder_details['primary_location']['item']['properties']['web_path'])
                    founder_primary_location_region.append(founder_details['primary_location']['item']['properties']['region'])
                    founder_primary_location_region_code2.append(founder_details['primary_location']['item']['properties']['region_code2'])
                    founder_primary_location_country.append(founder_details['primary_location']['item']['properties']['country'])
                    founder_primary_location_country_code2.append(founder_details['primary_location']['item']['properties']['country_code2'])
                    founder_primary_location_country_code3.append(founder_details['primary_location']['item']['properties']['country_code3'])
                    founder_primary_location_continent.append(founder_details['primary_location']['item']['properties']['continent'])
                    founder_primary_location_created_at.append(founder_details['primary_location']['item']['properties']['created_at'])
                    founder_primary_location_updated_at.append(founder_details['primary_location']['item']['properties']['updated_at'])
                else: # Else append as missing entries
                    founder_primary_location_type.append('')
                    founder_primary_location_uuid.append('')
                    founder_primary_location_location_type.append('')
                    founder_primary_location_parent_location_uuid.append('')
                    founder_primary_location_city.append('')
                    founder_primary_location_region.append('')
                    founder_primary_location_region_code2.append('')
                    founder_primary_location_country.append('')
                    founder_primary_location_country_code2.append('')
                    founder_primary_location_country_code3.append('')
                    founder_primary_location_continent.append('')
                    founder_primary_location_created_at.append('')
                    founder_primary_location_updated_at.append('')            
                    
                # Primary affiliations for each founder
                founder_primary_affiliation_total_items.append(founder_details['primary_affiliation']['paging']['total_items'])
                if founder_primary_affiliation_total_items[-1] >0: # If founder affiliation details are available, append the details
                    founder_primary_affiliation_type.append(founder_details['primary_affiliation']['item']['type'])
                    founder_primary_affiliation_uuid.append(founder_details['primary_affiliation']['item']['uuid'])
                    founder_primary_affiliation_title.append(founder_details['primary_affiliation']['item']['properties']['title'])
                    founder_primary_affiliation_started_on.append(founder_details['primary_affiliation']['item']['properties']['started_on'])
                    founder_primary_affiliation_started_on_trust_code.append(founder_details['primary_affiliation']['item']['properties']['started_on_trust_code'])
                    founder_primary_affiliation_ended_on.append(founder_details['primary_affiliation']['item']['properties']['ended_on'])
                    founder_primary_affiliation_ended_on_trust_code.append(founder_details['primary_affiliation']['item']['properties']['ended_on_trust_code'])            
                    founder_primary_affiliation_is_current.append(founder_details['primary_affiliation']['item']['properties']['is_current'])
                    founder_primary_affiliation_job_type.append(founder_details['primary_affiliation']['item']['properties']['job_type'])
                    founder_primary_affiliation_created_at.append(founder_details['primary_affiliation']['item']['properties']['created_at'])
                    founder_primary_affiliation_updated_at.append(founder_details['primary_affiliation']['item']['properties']['updated_at'])
                    founder_primary_affiliation_organization_type.append(founder_details['primary_affiliation']['item']['relationships']['organization']['type'])
                    founder_primary_affiliation_organization_uuid.append(founder_details['primary_affiliation']['item']['relationships']['organization']['uuid'])
                    founder_primary_affiliation_organization_permalink.append(founder_details['primary_affiliation']['item']['relationships']['organization']['properties']['permalink'])
                    founder_primary_affiliation_organization_permalink_aliases.append(founder_details['primary_affiliation']['item']['relationships']['organization']['properties']['permalink_aliases'])
                    founder_primary_affiliation_organization_api_path.append(founder_details['primary_affiliation']['item']['relationships']['organization']['properties']['api_path'])
                    founder_primary_affiliation_organization_web_path.append(founder_details['primary_affiliation']['item']['relationships']['organization']['properties']['web_path'])
                    founder_primary_affiliation_organization_api_url.append(founder_details['primary_affiliation']['item']['relationships']['organization']['properties']['api_url'])
                    founder_primary_affiliation_organization_name.append(founder_details['primary_affiliation']['item']['relationships']['organization']['properties']['name'])
                    founder_primary_affiliation_organization_also_known_as.append(founder_details['primary_affiliation']['item']['relationships']['organization']['properties']['also_known_as'])
                    founder_primary_affiliation_organization_short_description.append(founder_details['primary_affiliation']['item']['relationships']['organization']['properties']['short_description'])
                    founder_primary_affiliation_organization_description.append(founder_details['primary_affiliation']['item']['relationships']['organization']['properties']['description'])
                    founder_primary_affiliation_organization_profile_image_url.append(founder_details['primary_affiliation']['item']['relationships']['organization']['properties']['profile_image_url'])
                    founder_primary_affiliation_organization_primary_role.append(founder_details['primary_affiliation']['item']['relationships']['organization']['properties']['primary_role'])
                    founder_primary_affiliation_organization_role_company.append(founder_details['primary_affiliation']['item']['relationships']['organization']['properties']['role_company'])
                    founder_primary_affiliation_organization_role_investor.append(founder_details['primary_affiliation']['item']['relationships']['organization']['properties']['role_investor'])
                    founder_primary_affiliation_organization_role_group.append(founder_details['primary_affiliation']['item']['relationships']['organization']['properties']['role_group'])
                    founder_primary_affiliation_organization_role_school.append(founder_details['primary_affiliation']['item']['relationships']['organization']['properties']['role_school'])
                    founder_primary_affiliation_organization_investor_type.append(founder_details['primary_affiliation']['item']['relationships']['organization']['properties']['investor_type'])
                    founder_primary_affiliation_organization_founded_on.append(founder_details['primary_affiliation']['item']['relationships']['organization']['properties']['founded_on'])
                    founder_primary_affiliation_organization_founded_on_trust_code.append(founder_details['primary_affiliation']['item']['relationships']['organization']['properties']['founded_on_trust_code'])
                    founder_primary_affiliation_organization_is_closed.append(founder_details['primary_affiliation']['item']['relationships']['organization']['properties']['is_closed'])
                    founder_primary_affiliation_organization_closed_on.append(founder_details['primary_affiliation']['item']['relationships']['organization']['properties']['closed_on'])
                    founder_primary_affiliation_organization_closed_on_trust_code.append(founder_details['primary_affiliation']['item']['relationships']['organization']['properties']['closed_on_trust_code'])
                    founder_primary_affiliation_organization_num_employees_min.append(founder_details['primary_affiliation']['item']['relationships']['organization']['properties']['num_employees_min'])
                    founder_primary_affiliation_organization_num_employees_max.append(founder_details['primary_affiliation']['item']['relationships']['organization']['properties']['num_employees_max'])
                    founder_primary_affiliation_organization_stock_exchange.append(founder_details['primary_affiliation']['item']['relationships']['organization']['properties']['stock_exchange'])
                    founder_primary_affiliation_organization_stock_symbol.append(founder_details['primary_affiliation']['item']['relationships']['organization']['properties']['stock_symbol'])
                    founder_primary_affiliation_organization_total_funding_usd.append(founder_details['primary_affiliation']['item']['relationships']['organization']['properties']['total_funding_usd'])
                    founder_primary_affiliation_organization_number_of_investments.append(founder_details['primary_affiliation']['item']['relationships']['organization']['properties']['number_of_investments'])
                    founder_primary_affiliation_organization_homepage_url.append(founder_details['primary_affiliation']['item']['relationships']['organization']['properties']['homepage_url'])
                    founder_primary_affiliation_organization_contact_email.append(founder_details['primary_affiliation']['item']['relationships']['organization']['properties']['contact_email'])
                    founder_primary_affiliation_organization_phone_number.append(founder_details['primary_affiliation']['item']['relationships']['organization']['properties']['phone_number'])
                    founder_primary_affiliation_organization_rank.append(founder_details['primary_affiliation']['item']['relationships']['organization']['properties']['rank'])
                    founder_primary_affiliation_organization_created_at.append(founder_details['primary_affiliation']['item']['relationships']['organization']['properties']['created_at'])
                    founder_primary_affiliation_organization_updated_at.append(founder_details['primary_affiliation']['item']['relationships']['organization']['properties']['updated_at'])
                else: # Else append as missing entries
                    founder_primary_affiliation_type.append('')
                    founder_primary_affiliation_uuid.append('')
                    founder_primary_affiliation_title.append('')
                    founder_primary_affiliation_started_on.append('')
                    founder_primary_affiliation_started_on_trust_code.append('')
                    founder_primary_affiliation_ended_on.append('')
                    founder_primary_affiliation_ended_on_trust_code.append('')            
                    founder_primary_affiliation_is_current.append('')
                    founder_primary_affiliation_job_type.append('')
                    founder_primary_affiliation_created_at.append('')
                    founder_primary_affiliation_updated_at.append('')
                    founder_primary_affiliation_organization_type.append('')
                    founder_primary_affiliation_organization_uuid.append('')
                    founder_primary_affiliation_organization_permalink.append('')
                    founder_primary_affiliation_organization_permalink_aliases.append('')
                    founder_primary_affiliation_organization_api_path.append('')
                    founder_primary_affiliation_organization_web_path.append('')
                    founder_primary_affiliation_organization_api_url.append('')
                    founder_primary_affiliation_organization_name.append('')
                    founder_primary_affiliation_organization_also_known_as.append('')
                    founder_primary_affiliation_organization_short_description.append('')
                    founder_primary_affiliation_organization_description.append('')
                    founder_primary_affiliation_organization_profile_image_url.append('')
                    founder_primary_affiliation_organization_primary_role.append('')
                    founder_primary_affiliation_organization_role_company.append('')
                    founder_primary_affiliation_organization_role_investor.append('')
                    founder_primary_affiliation_organization_role_group.append('')
                    founder_primary_affiliation_organization_role_school.append('')
                    founder_primary_affiliation_organization_investor_type.append('')
                    founder_primary_affiliation_organization_founded_on.append('')
                    founder_primary_affiliation_organization_founded_on_trust_code.append('')
                    founder_primary_affiliation_organization_is_closed.append('')
                    founder_primary_affiliation_organization_closed_on.append('')
                    founder_primary_affiliation_organization_closed_on_trust_code.append('')
                    founder_primary_affiliation_organization_num_employees_min.append('')
                    founder_primary_affiliation_organization_num_employees_max.append('')
                    founder_primary_affiliation_organization_stock_exchange.append('')
                    founder_primary_affiliation_organization_stock_symbol.append('')
                    founder_primary_affiliation_organization_total_funding_usd.append('')
                    founder_primary_affiliation_organization_number_of_investments.append('')
                    founder_primary_affiliation_organization_homepage_url.append('')
                    founder_primary_affiliation_organization_contact_email.append('')
                    founder_primary_affiliation_organization_phone_number.append('')
                    founder_primary_affiliation_organization_rank.append('')
                    founder_primary_affiliation_organization_created_at.append('')
                    founder_primary_affiliation_organization_updated_at.append('')
                
                # Primary image details for each founder
                founder_primary_image_total_items.append(founder_details['primary_image']['paging']['total_items'])
                if founder_primary_image_total_items[-1] >0: # If founder primary image details are available, append the details
                    founder_primary_image_type.append(founder_details['primary_image']['item']['type'])
                    founder_primary_image_uuid.append(founder_details['primary_image']['item']['uuid'])
                    founder_primary_image_asset_path.append(founder_details['primary_image']['item']['properties']['asset_path'])
                    founder_primary_image_asset_url.append(founder_details['primary_image']['item']['properties']['asset_url'])
                    founder_primary_image_content_type.append(founder_details['primary_image']['item']['properties']['content_type'])
                    founder_primary_image_height.append(founder_details['primary_image']['item']['properties']['height'])
                    founder_primary_image_width.append(founder_details['primary_image']['item']['properties']['width'])
                    founder_primary_image_filesize.append(founder_details['primary_image']['item']['properties']['filesize'])
                    founder_primary_image_created_at.append(founder_details['primary_image']['item']['properties']['created_at'])
                    founder_primary_image_updated_at.append(founder_details['primary_image']['item']['properties']['updated_at'])
                else: # Else append as missing entries
                    founder_primary_image_type.append('')
                    founder_primary_image_uuid.append('')
                    founder_primary_image_asset_path.append('')
                    founder_primary_image_asset_url.append('')
                    founder_primary_image_content_type.append('')
                    founder_primary_image_height.append('')
                    founder_primary_image_width.append('')
                    founder_primary_image_filesize.append('')
                    founder_primary_image_created_at.append('')
                    founder_primary_image_updated_at.append('')
                
                # All degrees for each founder
                for founder_degrees in data_founder['data']['relationships']['degrees']['items']:
                    company_uuid_founder_degree.append(company_details['uuid'])
                    company_name_founder_degree.append(company_details['properties']['name'])
                    founder_uuid_founder_degree.append(founders_details['uuid'])
                    founder_first_name_founder_degree.append(founders_details['properties']['first_name'])
                    founder_last_name_founder_degree.append(founders_details['properties']['last_name'])
                    founder_degree_type.append(founder_degrees['type'])
                    founder_degree_uuid.append(founder_degrees['uuid'])
                    founder_degree_started_on.append(founder_degrees['properties']['started_on'])
                    founder_degree_started_on_trust_code.append(founder_degrees['properties']['started_on_trust_code'])
                    founder_degree_completed_on.append(founder_degrees['properties']['completed_on'])
                    founder_degree_completed_on_trust_code.append(founder_degrees['properties']['completed_on_trust_code'])
                    founder_degree_type_name.append(founder_degrees['properties']['degree_type_name'])
                    founder_degree_subject.append(founder_degrees['properties']['degree_subject'])
                    founder_degree_created_at.append(founder_degrees['properties']['created_at'])
                    founder_degree_updated_at.append(founder_degrees['properties']['updated_at'])
                    founder_degree_school_type.append(founder_degrees['relationships']['school']['type'])
                    founder_degree_school_uuid.append(founder_degrees['relationships']['school']['uuid'])
                    founder_degree_school_permalink.append(founder_degrees['relationships']['school']['properties']['permalink'])
                    founder_degree_school_permalink_aliases.append(founder_degrees['relationships']['school']['properties']['permalink_aliases'])
                    founder_degree_school_api_path.append(founder_degrees['relationships']['school']['properties']['api_path'])
                    founder_degree_school_web_path.append(founder_degrees['relationships']['school']['properties']['web_path'])
                    founder_degree_school_api_url.append(founder_degrees['relationships']['school']['properties']['api_url'])
                    founder_degree_school_name.append(founder_degrees['relationships']['school']['properties']['name'])
                    founder_degree_school_also_known_as.append(founder_degrees['relationships']['school']['properties']['also_known_as'])
                    founder_degree_school_short_description.append(founder_degrees['relationships']['school']['properties']['short_description'])
                    founder_degree_school_description.append(founder_degrees['relationships']['school']['properties']['description'])
                    founder_degree_school_profile_image_url.append(founder_degrees['relationships']['school']['properties']['profile_image_url'])
                    founder_degree_school_primary_role.append(founder_degrees['relationships']['school']['properties']['primary_role'])
                    founder_degree_school_role_company.append(founder_degrees['relationships']['school']['properties']['role_company'])
                    founder_degree_school_role_investor.append(founder_degrees['relationships']['school']['properties']['role_investor'])
                    founder_degree_school_role_group.append(founder_degrees['relationships']['school']['properties']['role_group'])
                    founder_degree_school_role_school.append(founder_degrees['relationships']['school']['properties']['role_school'])
                    founder_degree_school_investor_type.append(founder_degrees['relationships']['school']['properties']['investor_type'])
                    founder_degree_school_founded_on.append(founder_degrees['relationships']['school']['properties']['founded_on'])
                    founder_degree_school_founded_on_trust_code.append(founder_degrees['relationships']['school']['properties']['founded_on_trust_code'])
                    founder_degree_school_is_closed.append(founder_degrees['relationships']['school']['properties']['is_closed'])
                    founder_degree_school_closed_on.append(founder_degrees['relationships']['school']['properties']['closed_on'])
                    founder_degree_school_closed_on_trust_code.append(founder_degrees['relationships']['school']['properties']['closed_on_trust_code'])
                    founder_degree_school_num_employees_min.append(founder_degrees['relationships']['school']['properties']['num_employees_min'])
                    founder_degree_school_num_employees_max.append(founder_degrees['relationships']['school']['properties']['num_employees_max'])
                    founder_degree_school_stock_exchange.append(founder_degrees['relationships']['school']['properties']['stock_exchange'])
                    founder_degree_school_stock_symbol.append(founder_degrees['relationships']['school']['properties']['stock_symbol'])
                    founder_degree_school_total_funding_usd.append(founder_degrees['relationships']['school']['properties']['total_funding_usd'])
                    founder_degree_school_number_of_investments.append(founder_degrees['relationships']['school']['properties']['number_of_investments'])
                    founder_degree_school_homepage_url.append(founder_degrees['relationships']['school']['properties']['homepage_url'])
                    founder_degree_school_contact_email.append(founder_degrees['relationships']['school']['properties']['contact_email'])
                    founder_degree_school_phone_number.append(founder_degrees['relationships']['school']['properties']['phone_number'])
                    founder_degree_school_rank.append(founder_degrees['relationships']['school']['properties']['rank'])
                    founder_degree_school_created_at.append(founder_degrees['relationships']['school']['properties']['created_at'])
                    founder_degree_school_updated_at.append(founder_degrees['relationships']['school']['properties']['updated_at'])
                    
                # All jobs for each founder
                for founder_jobs in data_founder['data']['relationships']['jobs']['items']:
                    company_uuid_founder_job.append(company_details['uuid'])
                    company_name_founder_job.append(company_details['properties']['name'])
                    founder_uuid_founder_job.append(founders_details['uuid'])
                    founder_first_name_founder_job.append(founders_details['properties']['first_name'])
                    founder_last_name_founder_job.append(founders_details['properties']['last_name'])
                    founder_job_type.append(founder_jobs['type'])
                    founder_job_uuid.append(founder_jobs['uuid'])
                    founder_job_title.append(founder_jobs['properties']['title'])
                    founder_job_started_on.append(founder_jobs['properties']['started_on'])
                    founder_job_started_on_trust_code.append(founder_jobs['properties']['started_on_trust_code'])
                    founder_job_ended_on.append(founder_jobs['properties']['ended_on'])
                    founder_job_ended_on_trust_code.append(founder_jobs['properties']['ended_on_trust_code'])
                    founder_job_is_current.append(founder_jobs['properties']['is_current'])
                    founder_job_job_type.append(founder_jobs['properties']['job_type'])
                    founder_job_created_at.append(founder_jobs['properties']['created_at'])
                    founder_job_updated_at.append(founder_jobs['properties']['updated_at'])
                    founder_job_organization_type.append(founder_jobs['relationships']['organization']['type'])
                    founder_job_organization_uuid.append(founder_jobs['relationships']['organization']['uuid'])
                    founder_job_organization_permalink.append(founder_jobs['relationships']['organization']['properties']['permalink'])
                    founder_job_organization_permalink_aliases.append(founder_jobs['relationships']['organization']['properties']['permalink_aliases'])
                    founder_job_organization_api_path.append(founder_jobs['relationships']['organization']['properties']['api_path'])
                    founder_job_organization_web_path.append(founder_jobs['relationships']['organization']['properties']['web_path'])
                    founder_job_organization_api_url.append(founder_jobs['relationships']['organization']['properties']['api_url'])
                    founder_job_organization_name.append(founder_jobs['relationships']['organization']['properties']['name'])
                    founder_job_organization_also_known_as.append(founder_jobs['relationships']['organization']['properties']['also_known_as'])
                    founder_job_organization_short_description.append(founder_jobs['relationships']['organization']['properties']['short_description'])
                    founder_job_organization_description.append(founder_jobs['relationships']['organization']['properties']['description'])
                    founder_job_organization_profile_image_url.append(founder_jobs['relationships']['organization']['properties']['profile_image_url'])
                    founder_job_organization_primary_role.append(founder_jobs['relationships']['organization']['properties']['primary_role'])
                    founder_job_organization_role_company.append(founder_jobs['relationships']['organization']['properties']['role_company'])
                    founder_job_organization_role_investor.append(founder_jobs['relationships']['organization']['properties']['role_investor'])
                    founder_job_organization_role_group.append(founder_jobs['relationships']['organization']['properties']['role_group'])
                    founder_job_organization_role_school.append(founder_jobs['relationships']['organization']['properties']['role_school'])
                    founder_job_organization_investor_type.append(founder_jobs['relationships']['organization']['properties']['investor_type'])
                    founder_job_organization_founded_on.append(founder_jobs['relationships']['organization']['properties']['founded_on'])
                    founder_job_organization_founded_on_trust_code.append(founder_jobs['relationships']['organization']['properties']['founded_on_trust_code'])
                    founder_job_organization_is_closed.append(founder_jobs['relationships']['organization']['properties']['is_closed'])
                    founder_job_organization_closed_on.append(founder_jobs['relationships']['organization']['properties']['closed_on'])
                    founder_job_organization_closed_on_trust_code.append(founder_jobs['relationships']['organization']['properties']['closed_on_trust_code'])
                    founder_job_organization_num_employees_min.append(founder_jobs['relationships']['organization']['properties']['num_employees_min'])
                    founder_job_organization_num_employees_max.append(founder_jobs['relationships']['organization']['properties']['num_employees_max'])
                    founder_job_organization_stock_exchange.append(founder_jobs['relationships']['organization']['properties']['stock_exchange'])
                    founder_job_organization_stock_symbol.append(founder_jobs['relationships']['organization']['properties']['stock_symbol'])
                    founder_job_organization_total_funding_usd.append(founder_jobs['relationships']['organization']['properties']['total_funding_usd'])
                    founder_job_organization_number_of_investments.append(founder_jobs['relationships']['organization']['properties']['number_of_investments'])
                    founder_job_organization_homepage_url.append(founder_jobs['relationships']['organization']['properties']['homepage_url'])
                    founder_job_organization_contact_email.append(founder_jobs['relationships']['organization']['properties']['contact_email'])
                    founder_job_organization_phone_number.append(founder_jobs['relationships']['organization']['properties']['phone_number'])
                    founder_job_organization_rank.append(founder_jobs['relationships']['organization']['properties']['rank'])
                    founder_job_organization_created_at.append(founder_jobs['relationships']['organization']['properties']['created_at'])
                    founder_job_organization_updated_at.append(founder_jobs['relationships']['organization']['properties']['updated_at'])
                    
                # All companies founded by each fonder
                for founder_founded_companies in data_founder['data']['relationships']['founded_companies']['items']:
                    company_uuid_founder_founded_company.append(company_details['uuid'])
                    company_name_founder_founded_company.append(company_details['properties']['name'])
                    founder_uuid_founder_founded_company.append(founders_details['uuid'])
                    founder_first_name_founder_founded_company.append(founders_details['properties']['first_name'])
                    founder_last_name_founder_founded_company.append(founders_details['properties']['last_name'])
                    founder_founded_company_type.append(founder_founded_companies['type'])
                    founder_founded_company_uuid.append(founder_founded_companies['uuid'])
                    founder_founded_company_permalink.append(founder_founded_companies['properties']['permalink'])
                    founder_founded_company_permalink_aliases.append(founder_founded_companies['properties']['permalink_aliases'])
                    founder_founded_company_api_path.append(founder_founded_companies['properties']['api_path'])
                    founder_founded_company_web_path.append(founder_founded_companies['properties']['web_path'])
                    founder_founded_company_api_url.append(founder_founded_companies['properties']['api_url'])
                    founder_founded_company_name.append(founder_founded_companies['properties']['name'])
                    founder_founded_company_also_known_as.append(founder_founded_companies['properties']['also_known_as'])
                    founder_founded_company_short_description.append(founder_founded_companies['properties']['short_description'])
                    founder_founded_company_description.append(founder_founded_companies['properties']['description'])
                    founder_founded_company_profile_image_url.append(founder_founded_companies['properties']['profile_image_url'])
                    founder_founded_company_primary_role.append(founder_founded_companies['properties']['primary_role'])
                    founder_founded_company_role_company.append(founder_founded_companies['properties']['role_company'])
                    founder_founded_company_role_investor.append(founder_founded_companies['properties']['role_investor'])
                    founder_founded_company_role_group.append(founder_founded_companies['properties']['role_group'])
                    founder_founded_company_role_school.append(founder_founded_companies['properties']['role_school'])
                    founder_founded_company_investor_type.append(founder_founded_companies['properties']['investor_type'])
                    founder_founded_company_founded_on.append(founder_founded_companies['properties']['founded_on'])
                    founder_founded_company_founded_on_trust_code.append(founder_founded_companies['properties']['founded_on_trust_code'])
                    founder_founded_company_is_closed.append(founder_founded_companies['properties']['is_closed'])
                    founder_founded_company_closed_on.append(founder_founded_companies['properties']['closed_on'])
                    founder_founded_company_closed_on_trust_code.append(founder_founded_companies['properties']['closed_on_trust_code'])
                    founder_founded_company_num_employees_min.append(founder_founded_companies['properties']['num_employees_min'])
                    founder_founded_company_num_employees_max.append(founder_founded_companies['properties']['num_employees_max'])
                    founder_founded_company_stock_exchange.append(founder_founded_companies['properties']['stock_exchange'])
                    founder_founded_company_stock_symbol.append(founder_founded_companies['properties']['stock_symbol'])
                    founder_founded_company_total_funding_usd.append(founder_founded_companies['properties']['total_funding_usd'])
                    founder_founded_company_number_of_investments.append(founder_founded_companies['properties']['number_of_investments'])
                    founder_founded_company_homepage_url.append(founder_founded_companies['properties']['homepage_url'])
                    founder_founded_company_contact_email.append(founder_founded_companies['properties']['contact_email'])
                    founder_founded_company_phone_number.append(founder_founded_companies['properties']['phone_number'])
                    founder_founded_company_rank.append(founder_founded_companies['properties']['rank'])
                    founder_founded_company_created_at.append(founder_founded_companies['properties']['created_at'])
                    founder_founded_company_updated_at.append(founder_founded_companies['properties']['updated_at'])
                 
                    # All website urls (Facebook, Twitter, and LinkedIn) for each founder
                    founder_website_paging_total_items.append(founder_details['websites']['paging']['total_items'])
                    for founder_websites in data_founder['data']['relationships']['websites']['items']:
                        if founder_website_paging_total_items[-1]>0: # If founder website details are available, append the details
                            company_uuid_founder_website.append(company_details['uuid'])
                            company_name_founder_website.append(company_details['properties']['name'])
                            founder_uuid_founder_website.append(founders_details['uuid'])
                            founder_first_name_founder_website.append(founders_details['properties']['first_name'])
                            founder_last_name_founder_website.append(founders_details['properties']['last_name'])
                            founder_website_type.append(founder_websites['type'])
                            founder_website_uuid.append(founder_websites['uuid'])
                            founder_website_website_type.append(founder_websites['properties']['website_type'])
                            founder_website_website_name.append(founder_websites['properties']['website_name'])
                            founder_website_url.append(founder_websites['properties']['url'])
                            founder_website_created_at.append(founder_websites['properties']['created_at'])
                            founder_website_updated_at.append(founder_websites['properties']['updated_at'])                    
                        else: # Else append as missing entries
                            company_uuid_founder_website.append(company_details['uuid'])
                            company_name_founder_website.append(company_details['properties']['name'])
                            founder_uuid_founder_website.append(founders_details['uuid'])
                            founder_first_name_founder_website.append(founders_details['properties']['first_name'])
                            founder_last_name_founder_website.append(founders_details['properties']['last_name'])
                            founder_website_type.append('')
                            founder_website_uuid.append('')
                            founder_website_website_type.append('')
                            founder_website_website_name.append('')
                            founder_website_url.append('')
                            founder_website_created_at.append('')
                            founder_website_updated_at.append('')
                            
                    # All advisory roles for each founder
                    founder_advisory_roles_paging_total_items.append(founder_details['websites']['paging']['total_items'])
                    for founder_advisory_roles in data_founder['data']['relationships']['advisory_roles']['items']:
                        if founder_advisory_roles_paging_total_items[-1]>0: # If founder website details are available, append the details
                            company_uuid_founder_advisory_role.append(company_details['uuid'])
                            company_name_founder_advisory_role.append(company_details['properties']['name'])
                            founder_uuid_founder_advisory_role.append(founders_details['uuid'])
                            founder_first_name_founder_advisory_role.append(founders_details['properties']['first_name'])
                            founder_last_name_founder_advisory_role.append(founders_details['properties']['last_name'])
                            founder_advisory_role_type.append(founder_advisory_roles['type'])
                            founder_advisory_role_uuid.append(founder_advisory_roles['uuid'])
                            founder_advisory_role_title.append(founder_advisory_roles['properties']['title'])
                            founder_advisory_role_started_on.append(founder_advisory_roles['properties']['started_on'])
                            founder_advisory_role_started_on_trust_code.append(founder_advisory_roles['properties']['started_on_trust_code'])
                            founder_advisory_role_ended_on.append(founder_advisory_roles['properties']['ended_on'])
                            founder_advisory_role_ended_on_trust_code.append(founder_advisory_roles['properties']['ended_on_trust_code'])
                            founder_advisory_role_is_current.append(founder_advisory_roles['properties']['is_current'])
                            founder_advisory_role_job_type.append(founder_advisory_roles['properties']['job_type'])
                            founder_advisory_role_created_at.append(founder_advisory_roles['properties']['created_at'])
                            founder_advisory_role_updated_at.append(founder_advisory_roles['properties']['updated_at'])
                            founder_advisory_role_organization_permalink.append(founder_advisory_roles['relationships']['organization']['properties']['permalink'])
                            founder_advisory_role_organization_permalink_aliases.append(founder_advisory_roles['relationships']['organization']['properties']['permalink_aliases'])
                            founder_advisory_role_organization_api_path.append(founder_advisory_roles['relationships']['organization']['properties']['api_path'])
                            founder_advisory_role_organization_web_path.append(founder_advisory_roles['relationships']['organization']['properties']['web_path'])
                            founder_advisory_role_organization_api_url.append(founder_advisory_roles['relationships']['organization']['properties']['api_url'])
                            founder_advisory_role_organization_name.append(founder_advisory_roles['relationships']['organization']['properties']['name'])
                            founder_advisory_role_organization_also_known_as.append(founder_advisory_roles['relationships']['organization']['properties']['also_known_as'])
                            founder_advisory_role_organization_short_description.append(founder_advisory_roles['relationships']['organization']['properties']['short_description'])
                            founder_advisory_role_organization_description.append(founder_advisory_roles['relationships']['organization']['properties']['description'])
                            founder_advisory_role_organization_profile_image_url.append(founder_advisory_roles['relationships']['organization']['properties']['profile_image_url'])
                            founder_advisory_role_organization_primary_role.append(founder_advisory_roles['relationships']['organization']['properties']['primary_role'])
                            founder_advisory_role_organization_role_company.append(founder_advisory_roles['relationships']['organization']['properties']['role_company'])
                            founder_advisory_role_organization_role_investor.append(founder_advisory_roles['relationships']['organization']['properties']['role_investor'])
                            founder_advisory_role_organization_role_group.append(founder_advisory_roles['relationships']['organization']['properties']['role_group'])
                            founder_advisory_role_organization_role_school.append(founder_advisory_roles['relationships']['organization']['properties']['role_school'])
                            founder_advisory_role_organization_investor_type.append(founder_advisory_roles['relationships']['organization']['properties']['investor_type'])
                            founder_advisory_role_organization_founded_on.append(founder_advisory_roles['relationships']['organization']['properties']['founded_on'])
                            founder_advisory_role_organization_founded_on_trust_code.append(founder_advisory_roles['relationships']['organization']['properties']['founded_on_trust_code'])
                            founder_advisory_role_organization_is_closed.append(founder_advisory_roles['relationships']['organization']['properties']['is_closed'])
                            founder_advisory_role_organization_closed_on.append(founder_advisory_roles['relationships']['organization']['properties']['closed_on'])
                            founder_advisory_role_organization_closed_on_trust_code.append(founder_advisory_roles['relationships']['organization']['properties']['closed_on_trust_code'])
                            founder_advisory_role_organization_num_employees_min.append(founder_advisory_roles['relationships']['organization']['properties']['num_employees_min'])
                            founder_advisory_role_organization_num_employees_max.append(founder_advisory_roles['relationships']['organization']['properties']['num_employees_max'])
                            founder_advisory_role_organization_stock_exchange.append(founder_advisory_roles['relationships']['organization']['properties']['stock_exchange'])
                            founder_advisory_role_organization_stock_symbol.append(founder_advisory_roles['relationships']['organization']['properties']['stock_symbol'])
                            founder_advisory_role_organization_total_funding_usd.append(founder_advisory_roles['relationships']['organization']['properties']['total_funding_usd'])
                            founder_advisory_role_organization_number_of_investments.append(founder_advisory_roles['relationships']['organization']['properties']['number_of_investments'])
                            founder_advisory_role_organization_homepage_url.append(founder_advisory_roles['relationships']['organization']['properties']['homepage_url'])
                            founder_advisory_role_organization_contact_email.append(founder_advisory_roles['relationships']['organization']['properties']['contact_email'])
                            founder_advisory_role_organization_phone_number.append(founder_advisory_roles['relationships']['organization']['properties']['phone_number'])
                            founder_advisory_role_organization_rank.append(founder_advisory_roles['relationships']['organization']['properties']['rank'])
                            founder_advisory_role_organization_created_at.append(founder_advisory_roles['relationships']['organization']['properties']['created_at'])
                            founder_advisory_role_organization_updated_at.append(founder_advisory_roles['relationships']['organization']['properties']['updated_at'])
                            
                        else: # Else append as missing entries
                            company_uuid_founder_advisory_role.append(company_details['uuid'])
                            company_name_founder_advisory_role.append(company_details['properties']['name'])
                            founder_uuid_founder_advisory_role.append(founders_details['uuid'])
                            founder_first_name_founder_advisory_role.append(founders_details['properties']['first_name'])
                            founder_last_name_founder_advisory_role.append(founders_details['properties']['last_name'])
                            founder_advisory_role_type.append('')
                            founder_advisory_role_uuid.append('')
                            founder_advisory_role_title.append('')
                            founder_advisory_role_started_on.append('')
                            founder_advisory_role_started_on_trust_code.append('')
                            founder_advisory_role_ended_on.append('')
                            founder_advisory_role_ended_on_trust_code.append('')
                            founder_advisory_role_is_current.append('')
                            founder_advisory_role_job_type.append('')
                            founder_advisory_role_created_at.append('')
                            founder_advisory_role_updated_at.append('')
                            founder_advisory_role_organization_permalink.append('')
                            founder_advisory_role_organization_permalink_aliases.append('')
                            founder_advisory_role_organization_api_path.append('')
                            founder_advisory_role_organization_web_path.append('')
                            founder_advisory_role_organization_api_url.append('')
                            founder_advisory_role_organization_name.append('')
                            founder_advisory_role_organization_also_known_as.append('')
                            founder_advisory_role_organization_short_description.append('')
                            founder_advisory_role_organization_description.append('')
                            founder_advisory_role_organization_profile_image_url.append('')
                            founder_advisory_role_organization_primary_role.append('')
                            founder_advisory_role_organization_role_company.append('')
                            founder_advisory_role_organization_role_investor.append('')
                            founder_advisory_role_organization_role_group.append('')
                            founder_advisory_role_organization_role_school.append('')
                            founder_advisory_role_organization_investor_type.append('')
                            founder_advisory_role_organization_founded_on.append('')
                            founder_advisory_role_organization_founded_on_trust_code.append('')
                            founder_advisory_role_organization_is_closed.append('')
                            founder_advisory_role_organization_closed_on.append('')
                            founder_advisory_role_organization_closed_on_trust_code.append('')
                            founder_advisory_role_organization_num_employees_min.append('')
                            founder_advisory_role_organization_num_employees_max.append('')
                            founder_advisory_role_organization_stock_exchange.append('')
                            founder_advisory_role_organization_stock_symbol.append('')
                            founder_advisory_role_organization_total_funding_usd.append('')
                            founder_advisory_role_organization_number_of_investments.append('')
                            founder_advisory_role_organization_homepage_url.append('')
                            founder_advisory_role_organization_contact_email.append('')
                            founder_advisory_role_organization_phone_number.append('')
                            founder_advisory_role_organization_rank.append('')
                            founder_advisory_role_organization_created_at.append('')
                            founder_advisory_role_organization_updated_at.append('')
                    
                    # All investments made by each founder
                    founder_investments_paging_total_items.append(founder_details['investments']['paging']['total_items'])
                    if founder_investments_paging_total_items[-1]>0: # If founder website details are available, append the details
                        page=1
                        while page <= funding_paging_number_of_pages: # Pagination - For any item, CrunchBase API shows at most 100 entries per page. For items with over 100 entries, we have to scrape details from each page
                            founder_investments_url = founder_details['investments']['paging']['first_page_url'] + '?page={}&sort_order=announced_on%20DESC&items_per_page=100&user_key={}'.format(page, api_key)
                            
                            try:
                                response = urllib.request.urlopen(founder_investments_url, timeout=timeout_time_seconds)
                            except:
                                time_excep_founders_investment.append(url)
                                continue
                            data_founder_investments = json.loads(response.read().decode())
                            for founder_investments in data_founder_investments['data']['items']:
                                page = page+1
                                company_uuid_founder_investments.append(company_details['uuid'])
                                company_name_founder_investments.append(company_details['properties']['name'])
                                founder_uuid_founder_investments.append(founders_details['uuid'])
                                founder_first_name_investments.append(founders_details['properties']['first_name'])
                                founder_last_name_founder_investments.append(founders_details['properties']['last_name'])
                                founder_investment_type.append(founder_investments['type'])
                                founder_investment_uuid.append(founder_investments['uuid'])
                                founder_investment_money_invested.append(founder_investments['properties']['money_invested'])
                                founder_investment_money_invested_currency_code.append(founder_investments['properties']['money_invested_currency_code'])
                                founder_investment_money_invested_usd.append(founder_investments['properties']['money_invested_usd'])
                                founder_investment_is_lead_investor.append(founder_investments['properties']['is_lead_investor'])
                                founder_investment_announced_on.append(founder_investments['properties']['announced_on'])
                                founder_investment_announced_on_trust_code.append(founder_investments['properties']['announced_on_trust_code'])
                                founder_investment_created_at.append(founder_investments['properties']['created_at'])
                                founder_investment_updated_at.append(founder_investments['properties']['updated_at'])
                                founder_investment_funding_round_type.append(founder_investments['relationships']['funding_round']['type'])
                                founder_investment_funding_round_uuid.append(founder_investments['relationships']['funding_round']['uuid'])
                                founder_investment_funding_round_permalink.append(founder_investments['relationships']['funding_round']['properties']['permalink'])
                                founder_investment_funding_round_api_path.append(founder_investments['relationships']['funding_round']['properties']['api_path'])
                                founder_investment_funding_round_web_path.append(founder_investments['relationships']['funding_round']['properties']['web_path'])
                                founder_investment_funding_round_api_url.append(founder_investments['relationships']['funding_round']['properties']['api_url'])
                                founder_investment_funding_round_funding_type.append(founder_investments['relationships']['funding_round']['properties']['funding_type'])
                                founder_investment_funding_round_series.append(founder_investments['relationships']['funding_round']['properties']['series'])
                                founder_investment_funding_round_series_qualifier.append(founder_investments['relationships']['funding_round']['properties']['series_qualifier'])
                                founder_investment_funding_round_announced_on.append(founder_investments['relationships']['funding_round']['properties']['announced_on'])
                                founder_investment_funding_round_announced_on_trust_code.append(founder_investments['relationships']['funding_round']['properties']['announced_on_trust_code'])
                                founder_investment_funding_round_closed_on.append(founder_investments['relationships']['funding_round']['properties']['closed_on'])
                                founder_investment_funding_round_closed_on_trust_code.append(founder_investments['relationships']['funding_round']['properties']['closed_on_trust_code'])
                                founder_investment_funding_money_raised.append(founder_investments['relationships']['funding_round']['properties']['money_raised'])
                                founder_investment_funding_round_money_raised_currency_code.append(founder_investments['relationships']['funding_round']['properties']['money_raised_currency_code'])
                                founder_investment_funding_round_money_raised_usd.append(founder_investments['relationships']['funding_round']['properties']['money_raised_usd'])
                                founder_investment_funding_round_target_money_raised.append(founder_investments['relationships']['funding_round']['properties']['target_money_raised'])
                                founder_investment_funding_round_target_money_raised_currency_code.append(founder_investments['relationships']['funding_round']['properties']['target_money_raised_currency_code'])
                                founder_investment_funding_round_target_money_raised_usd.append(founder_investments['relationships']['funding_round']['properties']['target_money_raised_usd'])
                                founder_investment_funding_round_pre_money_valuation.append(founder_investments['relationships']['funding_round']['properties']['pre_money_valuation'])
                                founder_investment_funding_round_pre_money_valuation_currency_code.append(founder_investments['relationships']['funding_round']['properties']['pre_money_valuation_currency_code'])
                                founder_investment_funding_round_pre_money_valuation_usd.append(founder_investments['relationships']['funding_round']['properties']['pre_money_valuation_usd'])
                                founder_investment_funding_round_rank.append(founder_investments['relationships']['funding_round']['properties']['rank'])
                                founder_investment_funding_round_created_at.append(founder_investments['relationships']['funding_round']['properties']['created_at'])
                                founder_investment_funding_round_updated_at.append(founder_investments['relationships']['funding_round']['properties']['updated_at'])
                                founder_investment_funding_round_funded_organization_type.append(founder_investments['relationships']['funding_round']['relationships']['funded_organization']['type'])
                                founder_investment_funding_round_funded_organization_uuid.append(founder_investments['relationships']['funding_round']['relationships']['funded_organization']['uuid'])
                                founder_investment_funding_round_funded_organization_permalink.append(founder_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['permalink'])
                                founder_investment_funding_round_funded_organization_permalink_aliases.append(founder_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['permalink_aliases'])
                                founder_investment_funding_round_funded_organization_api_path.append(founder_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['api_path'])
                                founder_investment_funding_round_funded_organization_web_path.append(founder_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['web_path'])
                                founder_investment_funding_round_funded_organization_api_url.append(founder_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['api_url'])
                                founder_investment_funding_round_funded_organization_name.append(founder_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['name'])
                                founder_investment_funding_round_funded_organization_also_known_as.append(founder_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['also_known_as'])
                                founder_investment_funding_round_funded_organization_short_description.append(founder_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['short_description'])
                                founder_investment_funding_round_funded_organization_description.append(founder_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['description'])
                                founder_investment_funding_round_funded_organization_profile_image_url.append(founder_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['profile_image_url'])
                                founder_investment_funding_round_funded_organization_primary_role.append(founder_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['primary_role'])
                                founder_investment_funding_round_funded_organization_role_company.append(founder_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['role_company'])
                                founder_investment_funding_round_funded_organization_role_investor.append(founder_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['role_investor'])
                                founder_investment_funding_round_funded_organization_role_group.append(founder_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['role_group'])
                                founder_investment_funding_round_funded_organization_role_school.append(founder_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['role_school'])
                                founder_investment_funding_round_funded_organization_investor_type.append(founder_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['investor_type'])
                                founder_investment_funding_round_funded_organization_founded_on.append(founder_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['founded_on'])
                                founder_investment_funding_round_funded_organization_founded_on_trust_code.append(founder_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['founded_on_trust_code'])
                                founder_investment_funding_round_funded_organization_is_closed.append(founder_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['is_closed'])
                                founder_investment_funding_round_funded_organization_closed_on.append(founder_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['closed_on'])
                                founder_investment_funding_round_funded_organization_closed_on_trust_code.append(founder_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['closed_on_trust_code'])
                                founder_investment_funding_round_funded_organization_num_employees_min.append(founder_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['num_employees_min'])
                                founder_investment_funding_round_funded_organization_num_employees_max.append(founder_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['num_employees_max'])
                                founder_investment_funding_round_funded_organization_stock_exchange.append(founder_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['stock_exchange'])
                                founder_investment_funding_round_funded_organization_stock_symbol.append(founder_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['stock_symbol'])
                                founder_investment_funding_round_funded_organization_total_funding_usd.append(founder_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['total_funding_usd'])
                                founder_investment_funding_round_funded_organization_number_of_investments.append(founder_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['number_of_investments'])
                                founder_investment_funding_round_funded_organization_homepage_url.append(founder_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['homepage_url'])
                                founder_investment_funding_round_funded_organization_contact_email.append(founder_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['contact_email'])
                                founder_investment_funding_round_funded_organization_phone_number.append(founder_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['phone_number'])
                                founder_investment_funding_round_funded_organization_rank.append(founder_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['rank'])
                                founder_investment_funding_round_funded_organization_created_at.append(founder_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['created_at'])
                                founder_investment_funding_round_funded_organization_updated_at.append(founder_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['updated_at'])
                                
    
    
        # The following details are scraped for all founders of the company by going to the founders url
        board_url = company_details['relationships']['board_members_and_advisors']['paging']['first_page_url'] +'?user_key={}'.format(api_key)
       #company_board_url.append(board_url)
        try:
            response = urllib.request.urlopen(board_url, timeout=timeout_time_seconds)
        except:
            continue
        data_board = json.loads(response.read().decode())
        board_paging_number_of_pages= data_board['data']['paging']['number_of_pages']
        page_board=1
        while page_board <= board_paging_number_of_pages:
            BoardMembers_and_advisors_url = company_details['relationships']['board_members_and_advisors']['paging']['first_page_url'] + '?page={}&sort_order=announced_on%20DESC&items_per_page=100&user_key={}'.format(page_board, api_key)
            try:
                response = urllib.request.urlopen(board_url, timeout=timeout_time_seconds)
            except:
                continue
            data_board=json.loads(response.read().decode())
            page_board=page_board+1
            for board_details in data_board['data']['items']:
                company_uuid_board_details.append(company_details['uuid'])
                company_name_board_details.append(company_details['properties']['name'])                
                board_details_uuid.append(board_details['uuid'])
                board_details_title.append(board_details['properties']['title'])
                board_details_started_on.append(board_details['properties']['started_on'])
                board_details_started_on_trust_code.append(board_details['properties']['started_on_trust_code'])
                board_details_ended_on.append(board_details['properties']['ended_on'])
                board_details_ended_on_trust_code.append(board_details['properties']['ended_on_trust_code'])
                board_details_is_current.append(board_details['properties']['is_current'])
                board_details_job_type.append(board_details['properties']['job_type'])
                board_details_created_at.append(board_details['properties']['created_at'])
                board_details_updated_at.append(board_details['properties']['updated_at'])
                board_details_type.append(board_details['relationships']['person']['type'])
                board_details_person_uuid.append(board_details['relationships']['person']['uuid'])
                board_details_person_permalink.append(board_details['relationships']['person']['properties']['permalink'])
                board_details_person_permalink_aliases.append(board_details['relationships']['person']['properties']['permalink_aliases'])
                board_details_person_api_path.append(board_details['relationships']['person']['properties']['api_path'])
                board_details_person_web_path.append(board_details['relationships']['person']['properties']['web_path'])
                board_details_person_api_url.append(board_details['relationships']['person']['properties']['api_url'])
                board_details_person_first_name.append(board_details['relationships']['person']['properties']['first_name'])
                board_details_person_last_name.append(board_details['relationships']['person']['properties']['last_name'])
                board_details_person_gender.append(board_details['relationships']['person']['properties']['gender'])
                board_details_person_also_known_as.append(board_details['relationships']['person']['properties']['also_known_as'])
                board_details_person_bio.append(board_details['relationships']['person']['properties']['bio'])
                board_details_person_profile_image_url.append(board_details['relationships']['person']['properties']['profile_image_url'])
                board_details_person_role_investor.append(board_details['relationships']['person']['properties']['role_investor'])
                board_details_person_born_on.append(board_details['relationships']['person']['properties']['born_on'])
                board_details_person_born_on_trust_code.append(board_details['relationships']['person']['properties']['born_on_trust_code'])
                board_details_person_died_on.append(board_details['relationships']['person']['properties']['died_on'])
                board_details_person_died_on_trust_code.append(board_details['relationships']['person']['properties']['died_on_trust_code'])
                board_details_person_rank.append(board_details['relationships']['person']['properties']['rank'])
                board_details_person_created_at.append(board_details['relationships']['person']['properties']['created_at'])
                board_details_person_updated_at.append(board_details['relationships']['person']['properties']['updated_at'])
                
                BoardMembers_url= 'https://api.crunchbase.com/v3.1/people/{}?user_key={}'.format(board_details['relationships']['person']['uuid'], api_key)
                
                    
                try:
                    response = urllib.request.urlopen(BoardMembers_url, timeout=timeout_time_seconds)
                except:
                    timeout_excep_founder_details.append(url)
                    continue
                data_board_members = json.loads(response.read().decode())
                BoardMembers_details= data_board_members['data']['relationships']
                # Primary locations for each founder
                BoardMembers_primary_location_total_items.append(BoardMembers_details['primary_location']['paging']['total_items'])
                if BoardMembers_primary_location_total_items[-1] >0: # If board_members location details are available, append the details
                    BoardMembers_primary_location_type.append(BoardMembers_details['primary_location']['item']['type'])
                    BoardMembers_primary_location_uuid.append(BoardMembers_details['primary_location']['item']['uuid'])
                    BoardMembers_primary_location_location_type.append(BoardMembers_details['primary_location']['item']['properties']['location_type'])
                    BoardMembers_primary_location_parent_location_uuid.append(BoardMembers_details['primary_location']['item']['properties']['parent_location_uuid'])
                    BoardMembers_primary_location_city.append(BoardMembers_details['primary_location']['item']['properties']['web_path'])
                    BoardMembers_primary_location_region.append(BoardMembers_details['primary_location']['item']['properties']['region'])
                    BoardMembers_primary_location_region_code2.append(BoardMembers_details['primary_location']['item']['properties']['region_code2'])
                    BoardMembers_primary_location_country.append(BoardMembers_details['primary_location']['item']['properties']['country'])
                    BoardMembers_primary_location_country_code2.append(BoardMembers_details['primary_location']['item']['properties']['country_code2'])
                    BoardMembers_primary_location_country_code3.append(BoardMembers_details['primary_location']['item']['properties']['country_code3'])
                    BoardMembers_primary_location_continent.append(BoardMembers_details['primary_location']['item']['properties']['continent'])
                    BoardMembers_primary_location_created_at.append(BoardMembers_details['primary_location']['item']['properties']['created_at'])
                    BoardMembers_primary_location_updated_at.append(BoardMembers_details['primary_location']['item']['properties']['updated_at'])
                else: # Else append as missing entries
                    BoardMembers_primary_location_type.append('')
                    BoardMembers_primary_location_uuid.append('')
                    BoardMembers_primary_location_location_type.append('')
                    BoardMembers_primary_location_parent_location_uuid.append('')
                    BoardMembers_primary_location_city.append('')
                    BoardMembers_primary_location_region.append('')
                    BoardMembers_primary_location_region_code2.append('')
                    BoardMembers_primary_location_country.append('')
                    BoardMembers_primary_location_country_code2.append('')
                    BoardMembers_primary_location_country_code3.append('')
                    BoardMembers_primary_location_continent.append('')
                    BoardMembers_primary_location_created_at.append('')
                    BoardMembers_primary_location_updated_at.append('')            
                    
                # Primary affiliations for each board_members
                BoardMembers_primary_affiliation_total_items.append(BoardMembers_details['primary_affiliation']['paging']['total_items'])
                if BoardMembers_primary_affiliation_total_items[-1] >0: # If board_members affiliation details are available, append the details
                    BoardMembers_primary_affiliation_type.append(BoardMembers_details['primary_affiliation']['item']['type'])
                    BoardMembers_primary_affiliation_uuid.append(BoardMembers_details['primary_affiliation']['item']['uuid'])
                    BoardMembers_primary_affiliation_title.append(BoardMembers_details['primary_affiliation']['item']['properties']['title'])
                    BoardMembers_primary_affiliation_started_on.append(BoardMembers_details['primary_affiliation']['item']['properties']['started_on'])
                    BoardMembers_primary_affiliation_started_on_trust_code.append(BoardMembers_details['primary_affiliation']['item']['properties']['started_on_trust_code'])
                    BoardMembers_primary_affiliation_ended_on.append(BoardMembers_details['primary_affiliation']['item']['properties']['ended_on'])
                    BoardMembers_primary_affiliation_ended_on_trust_code.append(BoardMembers_details['primary_affiliation']['item']['properties']['ended_on_trust_code'])            
                    BoardMembers_primary_affiliation_is_current.append(BoardMembers_details['primary_affiliation']['item']['properties']['is_current'])
                    BoardMembers_primary_affiliation_job_type.append(BoardMembers_details['primary_affiliation']['item']['properties']['job_type'])
                    BoardMembers_primary_affiliation_created_at.append(BoardMembers_details['primary_affiliation']['item']['properties']['created_at'])
                    BoardMembers_primary_affiliation_updated_at.append(BoardMembers_details['primary_affiliation']['item']['properties']['updated_at'])
                    BoardMembers_primary_affiliation_organization_type.append(BoardMembers_details['primary_affiliation']['item']['relationships']['organization']['type'])
                    BoardMembers_primary_affiliation_organization_uuid.append(BoardMembers_details['primary_affiliation']['item']['relationships']['organization']['uuid'])
                    BoardMembers_primary_affiliation_organization_permalink.append(BoardMembers_details['primary_affiliation']['item']['relationships']['organization']['properties']['permalink'])
                    BoardMembers_primary_affiliation_organization_permalink_aliases.append(BoardMembers_details['primary_affiliation']['item']['relationships']['organization']['properties']['permalink_aliases'])
                    BoardMembers_primary_affiliation_organization_api_path.append(BoardMembers_details['primary_affiliation']['item']['relationships']['organization']['properties']['api_path'])
                    BoardMembers_primary_affiliation_organization_web_path.append(BoardMembers_details['primary_affiliation']['item']['relationships']['organization']['properties']['web_path'])
                    BoardMembers_primary_affiliation_organization_api_url.append(BoardMembers_details['primary_affiliation']['item']['relationships']['organization']['properties']['api_url'])
                    BoardMembers_primary_affiliation_organization_name.append(BoardMembers_details['primary_affiliation']['item']['relationships']['organization']['properties']['name'])
                    BoardMembers_primary_affiliation_organization_also_known_as.append(BoardMembers_details['primary_affiliation']['item']['relationships']['organization']['properties']['also_known_as'])
                    BoardMembers_primary_affiliation_organization_short_description.append(BoardMembers_details['primary_affiliation']['item']['relationships']['organization']['properties']['short_description'])
                    BoardMembers_primary_affiliation_organization_description.append(BoardMembers_details['primary_affiliation']['item']['relationships']['organization']['properties']['description'])
                    BoardMembers_primary_affiliation_organization_profile_image_url.append(BoardMembers_details['primary_affiliation']['item']['relationships']['organization']['properties']['profile_image_url'])
                    BoardMembers_primary_affiliation_organization_primary_role.append(BoardMembers_details['primary_affiliation']['item']['relationships']['organization']['properties']['primary_role'])
                    BoardMembers_primary_affiliation_organization_role_company.append(BoardMembers_details['primary_affiliation']['item']['relationships']['organization']['properties']['role_company'])
                    BoardMembers_primary_affiliation_organization_role_investor.append(BoardMembers_details['primary_affiliation']['item']['relationships']['organization']['properties']['role_investor'])
                    BoardMembers_primary_affiliation_organization_role_group.append(BoardMembers_details['primary_affiliation']['item']['relationships']['organization']['properties']['role_group'])
                    BoardMembers_primary_affiliation_organization_role_school.append(BoardMembers_details['primary_affiliation']['item']['relationships']['organization']['properties']['role_school'])
                    BoardMembers_primary_affiliation_organization_investor_type.append(BoardMembers_details['primary_affiliation']['item']['relationships']['organization']['properties']['investor_type'])
                    BoardMembers_primary_affiliation_organization_founded_on.append(BoardMembers_details['primary_affiliation']['item']['relationships']['organization']['properties']['founded_on'])
                    BoardMembers_primary_affiliation_organization_founded_on_trust_code.append(BoardMembers_details['primary_affiliation']['item']['relationships']['organization']['properties']['founded_on_trust_code'])
                    BoardMembers_primary_affiliation_organization_is_closed.append(BoardMembers_details['primary_affiliation']['item']['relationships']['organization']['properties']['is_closed'])
                    BoardMembers_primary_affiliation_organization_closed_on.append(BoardMembers_details['primary_affiliation']['item']['relationships']['organization']['properties']['closed_on'])
                    BoardMembers_primary_affiliation_organization_closed_on_trust_code.append(BoardMembers_details['primary_affiliation']['item']['relationships']['organization']['properties']['closed_on_trust_code'])
                    BoardMembers_primary_affiliation_organization_num_employees_min.append(BoardMembers_details['primary_affiliation']['item']['relationships']['organization']['properties']['num_employees_min'])
                    BoardMembers_primary_affiliation_organization_num_employees_max.append(BoardMembers_details['primary_affiliation']['item']['relationships']['organization']['properties']['num_employees_max'])
                    BoardMembers_primary_affiliation_organization_stock_exchange.append(BoardMembers_details['primary_affiliation']['item']['relationships']['organization']['properties']['stock_exchange'])
                    BoardMembers_primary_affiliation_organization_stock_symbol.append(BoardMembers_details['primary_affiliation']['item']['relationships']['organization']['properties']['stock_symbol'])
                    BoardMembers_primary_affiliation_organization_total_funding_usd.append(BoardMembers_details['primary_affiliation']['item']['relationships']['organization']['properties']['total_funding_usd'])
                    BoardMembers_primary_affiliation_organization_number_of_investments.append(BoardMembers_details['primary_affiliation']['item']['relationships']['organization']['properties']['number_of_investments'])
                    BoardMembers_primary_affiliation_organization_homepage_url.append(BoardMembers_details['primary_affiliation']['item']['relationships']['organization']['properties']['homepage_url'])
                    BoardMembers_primary_affiliation_organization_contact_email.append(BoardMembers_details['primary_affiliation']['item']['relationships']['organization']['properties']['contact_email'])
                    BoardMembers_primary_affiliation_organization_phone_number.append(BoardMembers_details['primary_affiliation']['item']['relationships']['organization']['properties']['phone_number'])
                    BoardMembers_primary_affiliation_organization_rank.append(BoardMembers_details['primary_affiliation']['item']['relationships']['organization']['properties']['rank'])
                    BoardMembers_primary_affiliation_organization_created_at.append(BoardMembers_details['primary_affiliation']['item']['relationships']['organization']['properties']['created_at'])
                    BoardMembers_primary_affiliation_organization_updated_at.append(BoardMembers_details['primary_affiliation']['item']['relationships']['organization']['properties']['updated_at'])
                else: # Else append as missing entries
                    BoardMembers_primary_affiliation_type.append('')
                    BoardMembers_primary_affiliation_uuid.append('')
                    BoardMembers_primary_affiliation_title.append('')
                    BoardMembers_primary_affiliation_started_on.append('')
                    BoardMembers_primary_affiliation_started_on_trust_code.append('')
                    BoardMembers_primary_affiliation_ended_on.append('')
                    BoardMembers_primary_affiliation_ended_on_trust_code.append('')            
                    BoardMembers_primary_affiliation_is_current.append('')
                    BoardMembers_primary_affiliation_job_type.append('')
                    BoardMembers_primary_affiliation_created_at.append('')
                    BoardMembers_primary_affiliation_updated_at.append('')
                    BoardMembers_primary_affiliation_organization_type.append('')
                    BoardMembers_primary_affiliation_organization_uuid.append('')
                    BoardMembers_primary_affiliation_organization_permalink.append('')
                    BoardMembers_primary_affiliation_organization_permalink_aliases.append('')
                    BoardMembers_primary_affiliation_organization_api_path.append('')
                    BoardMembers_primary_affiliation_organization_web_path.append('')
                    BoardMembers_primary_affiliation_organization_api_url.append('')
                    BoardMembers_primary_affiliation_organization_name.append('')
                    BoardMembers_primary_affiliation_organization_also_known_as.append('')
                    BoardMembers_primary_affiliation_organization_short_description.append('')
                    BoardMembers_primary_affiliation_organization_description.append('')
                    BoardMembers_primary_affiliation_organization_profile_image_url.append('')
                    BoardMembers_primary_affiliation_organization_primary_role.append('')
                    BoardMembers_primary_affiliation_organization_role_company.append('')
                    BoardMembers_primary_affiliation_organization_role_investor.append('')
                    BoardMembers_primary_affiliation_organization_role_group.append('')
                    BoardMembers_primary_affiliation_organization_role_school.append('')
                    BoardMembers_primary_affiliation_organization_investor_type.append('')
                    BoardMembers_primary_affiliation_organization_founded_on.append('')
                    BoardMembers_primary_affiliation_organization_founded_on_trust_code.append('')
                    BoardMembers_primary_affiliation_organization_is_closed.append('')
                    BoardMembers_primary_affiliation_organization_closed_on.append('')
                    BoardMembers_primary_affiliation_organization_closed_on_trust_code.append('')
                    BoardMembers_primary_affiliation_organization_num_employees_min.append('')
                    BoardMembers_primary_affiliation_organization_num_employees_max.append('')
                    BoardMembers_primary_affiliation_organization_stock_exchange.append('')
                    BoardMembers_primary_affiliation_organization_stock_symbol.append('')
                    BoardMembers_primary_affiliation_organization_total_funding_usd.append('')
                    BoardMembers_primary_affiliation_organization_number_of_investments.append('')
                    BoardMembers_primary_affiliation_organization_homepage_url.append('')
                    BoardMembers_primary_affiliation_organization_contact_email.append('')
                    BoardMembers_primary_affiliation_organization_phone_number.append('')
                    BoardMembers_primary_affiliation_organization_rank.append('')
                    BoardMembers_primary_affiliation_organization_created_at.append('')
                    BoardMembers_primary_affiliation_organization_updated_at.append('')
                
                # Primary image details for each board_members
                BoardMembers_primary_image_total_items.append(BoardMembers_details['primary_image']['paging']['total_items'])
                if BoardMembers_primary_image_total_items[-1] >0: # If board_members primary image details are available, append the details
                    BoardMembers_primary_image_type.append(BoardMembers_details['primary_image']['item']['type'])
                    BoardMembers_primary_image_uuid.append(BoardMembers_details['primary_image']['item']['uuid'])
                    BoardMembers_primary_image_asset_path.append(BoardMembers_details['primary_image']['item']['properties']['asset_path'])
                    BoardMembers_primary_image_asset_url.append(BoardMembers_details['primary_image']['item']['properties']['asset_url'])
                    BoardMembers_primary_image_content_type.append(BoardMembers_details['primary_image']['item']['properties']['content_type'])
                    BoardMembers_primary_image_height.append(BoardMembers_details['primary_image']['item']['properties']['height'])
                    BoardMembers_primary_image_width.append(BoardMembers_details['primary_image']['item']['properties']['width'])
                    BoardMembers_primary_image_filesize.append(BoardMembers_details['primary_image']['item']['properties']['filesize'])
                    BoardMembers_primary_image_created_at.append(BoardMembers_details['primary_image']['item']['properties']['created_at'])
                    BoardMembers_primary_image_updated_at.append(BoardMembers_details['primary_image']['item']['properties']['updated_at'])
                else: # Else append as missing entries
                    BoardMembers_primary_image_type.append('')
                    BoardMembers_primary_image_uuid.append('')
                    BoardMembers_primary_image_asset_path.append('')
                    BoardMembers_primary_image_asset_url.append('')
                    BoardMembers_primary_image_content_type.append('')
                    BoardMembers_primary_image_height.append('')
                    BoardMembers_primary_image_width.append('')
                    BoardMembers_primary_image_filesize.append('')
                    BoardMembers_primary_image_created_at.append('')
                    BoardMembers_primary_image_updated_at.append('')
                
                # All degrees for each board_members
                for BoardMembers_degrees in data_board_members['data']['relationships']['degrees']['items']:
                    company_uuid_BoardMembers_degree.append(company_details['uuid'])
                    company_name_BoardMembers_degree.append(company_details['properties']['name'])
                    BoardMembers_uuid_BoardMembers_degree.append(board_details['uuid'])
                    BoardMembers_first_name_BoardMembers_degree.append(board_details['relationships']['person']['properties']['first_name'])
                    BoardMembers_last_name_BoardMembers_degree.append(board_details['relationships']['person']['properties']['last_name'])
                    BoardMembers_degree_type.append(BoardMembers_degrees['type'])
                    BoardMembers_degree_uuid.append(BoardMembers_degrees['uuid'])
                    BoardMembers_degree_started_on.append(BoardMembers_degrees['properties']['started_on'])
                    BoardMembers_degree_started_on_trust_code.append(BoardMembers_degrees['properties']['started_on_trust_code'])
                    BoardMembers_degree_completed_on.append(BoardMembers_degrees['properties']['completed_on'])
                    BoardMembers_degree_completed_on_trust_code.append(BoardMembers_degrees['properties']['completed_on_trust_code'])
                    BoardMembers_degree_type_name.append(BoardMembers_degrees['properties']['degree_type_name'])
                    BoardMembers_degree_subject.append(BoardMembers_degrees['properties']['degree_subject'])
                    BoardMembers_degree_created_at.append(BoardMembers_degrees['properties']['created_at'])
                    BoardMembers_degree_updated_at.append(BoardMembers_degrees['properties']['updated_at'])
                    BoardMembers_degree_school_type.append(BoardMembers_degrees['relationships']['school']['type'])
                    BoardMembers_degree_school_uuid.append(BoardMembers_degrees['relationships']['school']['uuid'])
                    BoardMembers_degree_school_permalink.append(BoardMembers_degrees['relationships']['school']['properties']['permalink'])
                    BoardMembers_degree_school_permalink_aliases.append(BoardMembers_degrees['relationships']['school']['properties']['permalink_aliases'])
                    BoardMembers_degree_school_api_path.append(BoardMembers_degrees['relationships']['school']['properties']['api_path'])
                    BoardMembers_degree_school_web_path.append(BoardMembers_degrees['relationships']['school']['properties']['web_path'])
                    BoardMembers_degree_school_api_url.append(BoardMembers_degrees['relationships']['school']['properties']['api_url'])
                    BoardMembers_degree_school_name.append(BoardMembers_degrees['relationships']['school']['properties']['name'])
                    BoardMembers_degree_school_also_known_as.append(BoardMembers_degrees['relationships']['school']['properties']['also_known_as'])
                    BoardMembers_degree_school_short_description.append(BoardMembers_degrees['relationships']['school']['properties']['short_description'])
                    BoardMembers_degree_school_description.append(BoardMembers_degrees['relationships']['school']['properties']['description'])
                    BoardMembers_degree_school_profile_image_url.append(BoardMembers_degrees['relationships']['school']['properties']['profile_image_url'])
                    BoardMembers_degree_school_primary_role.append(BoardMembers_degrees['relationships']['school']['properties']['primary_role'])
                    BoardMembers_degree_school_role_company.append(BoardMembers_degrees['relationships']['school']['properties']['role_company'])
                    BoardMembers_degree_school_role_investor.append(BoardMembers_degrees['relationships']['school']['properties']['role_investor'])
                    BoardMembers_degree_school_role_group.append(BoardMembers_degrees['relationships']['school']['properties']['role_group'])
                    BoardMembers_degree_school_role_school.append(BoardMembers_degrees['relationships']['school']['properties']['role_school'])
                    BoardMembers_degree_school_investor_type.append(BoardMembers_degrees['relationships']['school']['properties']['investor_type'])
                    BoardMembers_degree_school_founded_on.append(BoardMembers_degrees['relationships']['school']['properties']['founded_on'])
                    BoardMembers_degree_school_founded_on_trust_code.append(BoardMembers_degrees['relationships']['school']['properties']['founded_on_trust_code'])
                    BoardMembers_degree_school_is_closed.append(BoardMembers_degrees['relationships']['school']['properties']['is_closed'])
                    BoardMembers_degree_school_closed_on.append(BoardMembers_degrees['relationships']['school']['properties']['closed_on'])
                    BoardMembers_degree_school_closed_on_trust_code.append(BoardMembers_degrees['relationships']['school']['properties']['closed_on_trust_code'])
                    BoardMembers_degree_school_num_employees_min.append(BoardMembers_degrees['relationships']['school']['properties']['num_employees_min'])
                    BoardMembers_degree_school_num_employees_max.append(BoardMembers_degrees['relationships']['school']['properties']['num_employees_max'])
                    BoardMembers_degree_school_stock_exchange.append(BoardMembers_degrees['relationships']['school']['properties']['stock_exchange'])
                    BoardMembers_degree_school_stock_symbol.append(BoardMembers_degrees['relationships']['school']['properties']['stock_symbol'])
                    BoardMembers_degree_school_total_funding_usd.append(BoardMembers_degrees['relationships']['school']['properties']['total_funding_usd'])
                    BoardMembers_degree_school_number_of_investments.append(BoardMembers_degrees['relationships']['school']['properties']['number_of_investments'])
                    BoardMembers_degree_school_homepage_url.append(BoardMembers_degrees['relationships']['school']['properties']['homepage_url'])
                    BoardMembers_degree_school_contact_email.append(BoardMembers_degrees['relationships']['school']['properties']['contact_email'])
                    BoardMembers_degree_school_phone_number.append(BoardMembers_degrees['relationships']['school']['properties']['phone_number'])
                    BoardMembers_degree_school_rank.append(BoardMembers_degrees['relationships']['school']['properties']['rank'])
                    BoardMembers_degree_school_created_at.append(BoardMembers_degrees['relationships']['school']['properties']['created_at'])
                    BoardMembers_degree_school_updated_at.append(BoardMembers_degrees['relationships']['school']['properties']['updated_at'])
                    
                # All jobs for each board_members
                for BoardMembers_jobs in data_board_members['data']['relationships']['jobs']['items']:
                    company_uuid_BoardMembers_job.append(company_details['uuid'])
                    company_name_BoardMembers_job.append(company_details['properties']['name'])
                    BoardMembers_uuid_BoardMembers_job.append(board_details['uuid'])
                    BoardMembers_first_name_BoardMembers_job.append(board_details['relationships']['person']['properties']['first_name'])
                    BoardMembers_last_name_BoardMembers_job.append(board_details['relationships']['person']['properties']['last_name'])
                    BoardMembers_job_type.append(BoardMembers_jobs['type'])
                    BoardMembers_job_uuid.append(BoardMembers_jobs['uuid'])
                    BoardMembers_job_title.append(BoardMembers_jobs['properties']['title'])
                    BoardMembers_job_started_on.append(BoardMembers_jobs['properties']['started_on'])
                    BoardMembers_job_started_on_trust_code.append(BoardMembers_jobs['properties']['started_on_trust_code'])
                    BoardMembers_job_ended_on.append(BoardMembers_jobs['properties']['ended_on'])
                    BoardMembers_job_ended_on_trust_code.append(BoardMembers_jobs['properties']['ended_on_trust_code'])
                    BoardMembers_job_is_current.append(BoardMembers_jobs['properties']['is_current'])
                    BoardMembers_job_job_type.append(BoardMembers_jobs['properties']['job_type'])
                    BoardMembers_job_created_at.append(BoardMembers_jobs['properties']['created_at'])
                    BoardMembers_job_updated_at.append(BoardMembers_jobs['properties']['updated_at'])
                    BoardMembers_job_organization_type.append(BoardMembers_jobs['relationships']['organization']['type'])
                    BoardMembers_job_organization_uuid.append(BoardMembers_jobs['relationships']['organization']['uuid'])
                    BoardMembers_job_organization_permalink.append(BoardMembers_jobs['relationships']['organization']['properties']['permalink'])
                    BoardMembers_job_organization_permalink_aliases.append(BoardMembers_jobs['relationships']['organization']['properties']['permalink_aliases'])
                    BoardMembers_job_organization_api_path.append(BoardMembers_jobs['relationships']['organization']['properties']['api_path'])
                    BoardMembers_job_organization_web_path.append(BoardMembers_jobs['relationships']['organization']['properties']['web_path'])
                    BoardMembers_job_organization_api_url.append(BoardMembers_jobs['relationships']['organization']['properties']['api_url'])
                    BoardMembers_job_organization_name.append(BoardMembers_jobs['relationships']['organization']['properties']['name'])
                    BoardMembers_job_organization_also_known_as.append(BoardMembers_jobs['relationships']['organization']['properties']['also_known_as'])
                    BoardMembers_job_organization_short_description.append(BoardMembers_jobs['relationships']['organization']['properties']['short_description'])
                    BoardMembers_job_organization_description.append(BoardMembers_jobs['relationships']['organization']['properties']['description'])
                    BoardMembers_job_organization_profile_image_url.append(BoardMembers_jobs['relationships']['organization']['properties']['profile_image_url'])
                    BoardMembers_job_organization_primary_role.append(BoardMembers_jobs['relationships']['organization']['properties']['primary_role'])
                    BoardMembers_job_organization_role_company.append(BoardMembers_jobs['relationships']['organization']['properties']['role_company'])
                    BoardMembers_job_organization_role_investor.append(BoardMembers_jobs['relationships']['organization']['properties']['role_investor'])
                    BoardMembers_job_organization_role_group.append(BoardMembers_jobs['relationships']['organization']['properties']['role_group'])
                    BoardMembers_job_organization_role_school.append(BoardMembers_jobs['relationships']['organization']['properties']['role_school'])
                    BoardMembers_job_organization_investor_type.append(BoardMembers_jobs['relationships']['organization']['properties']['investor_type'])
                    BoardMembers_job_organization_founded_on.append(BoardMembers_jobs['relationships']['organization']['properties']['founded_on'])
                    BoardMembers_job_organization_founded_on_trust_code.append(BoardMembers_jobs['relationships']['organization']['properties']['founded_on_trust_code'])
                    BoardMembers_job_organization_is_closed.append(BoardMembers_jobs['relationships']['organization']['properties']['is_closed'])
                    BoardMembers_job_organization_closed_on.append(BoardMembers_jobs['relationships']['organization']['properties']['closed_on'])
                    BoardMembers_job_organization_closed_on_trust_code.append(BoardMembers_jobs['relationships']['organization']['properties']['closed_on_trust_code'])
                    BoardMembers_job_organization_num_employees_min.append(BoardMembers_jobs['relationships']['organization']['properties']['num_employees_min'])
                    BoardMembers_job_organization_num_employees_max.append(BoardMembers_jobs['relationships']['organization']['properties']['num_employees_max'])
                    BoardMembers_job_organization_stock_exchange.append(BoardMembers_jobs['relationships']['organization']['properties']['stock_exchange'])
                    BoardMembers_job_organization_stock_symbol.append(BoardMembers_jobs['relationships']['organization']['properties']['stock_symbol'])
                    BoardMembers_job_organization_total_funding_usd.append(BoardMembers_jobs['relationships']['organization']['properties']['total_funding_usd'])
                    BoardMembers_job_organization_number_of_investments.append(BoardMembers_jobs['relationships']['organization']['properties']['number_of_investments'])
                    BoardMembers_job_organization_homepage_url.append(BoardMembers_jobs['relationships']['organization']['properties']['homepage_url'])
                    BoardMembers_job_organization_contact_email.append(BoardMembers_jobs['relationships']['organization']['properties']['contact_email'])
                    BoardMembers_job_organization_phone_number.append(BoardMembers_jobs['relationships']['organization']['properties']['phone_number'])
                    BoardMembers_job_organization_rank.append(BoardMembers_jobs['relationships']['organization']['properties']['rank'])
                    BoardMembers_job_organization_created_at.append(BoardMembers_jobs['relationships']['organization']['properties']['created_at'])
                    BoardMembers_job_organization_updated_at.append(BoardMembers_jobs['relationships']['organization']['properties']['updated_at'])
                    
                # All companies founded by each fonder
                for BoardMembers_founded_companies in data_board_members['data']['relationships']['founded_companies']['items']:
                    company_uuid_BoardMembers_founded_company.append(company_details['uuid'])
                    company_name_BoardMembers_founded_company.append(company_details['properties']['name'])
                    BoardMembers_uuid_BoardMembers_founded_company.append(board_details['uuid'])
                    BoardMembers_first_name_BoardMembers_founded_company.append(board_details['relationships']['person']['properties']['first_name'])
                    BoardMembers_last_name_BoardMembers_founded_company.append(board_details['relationships']['person']['properties']['last_name'])
                    BoardMembers_founded_company_type.append(BoardMembers_founded_companies['type'])
                    BoardMembers_founded_company_uuid.append(BoardMembers_founded_companies['uuid'])
                    BoardMembers_founded_company_permalink.append(BoardMembers_founded_companies['properties']['permalink'])
                    BoardMembers_founded_company_permalink_aliases.append(BoardMembers_founded_companies['properties']['permalink_aliases'])
                    BoardMembers_founded_company_api_path.append(BoardMembers_founded_companies['properties']['api_path'])
                    BoardMembers_founded_company_web_path.append(BoardMembers_founded_companies['properties']['web_path'])
                    BoardMembers_founded_company_api_url.append(BoardMembers_founded_companies['properties']['api_url'])
                    BoardMembers_founded_company_name.append(BoardMembers_founded_companies['properties']['name'])
                    BoardMembers_founded_company_also_known_as.append(BoardMembers_founded_companies['properties']['also_known_as'])
                    BoardMembers_founded_company_short_description.append(BoardMembers_founded_companies['properties']['short_description'])
                    BoardMembers_founded_company_description.append(BoardMembers_founded_companies['properties']['description'])
                    BoardMembers_founded_company_profile_image_url.append(BoardMembers_founded_companies['properties']['profile_image_url'])
                    BoardMembers_founded_company_primary_role.append(BoardMembers_founded_companies['properties']['primary_role'])
                    BoardMembers_founded_company_role_company.append(BoardMembers_founded_companies['properties']['role_company'])
                    BoardMembers_founded_company_role_investor.append(BoardMembers_founded_companies['properties']['role_investor'])
                    BoardMembers_founded_company_role_group.append(BoardMembers_founded_companies['properties']['role_group'])
                    BoardMembers_founded_company_role_school.append(BoardMembers_founded_companies['properties']['role_school'])
                    BoardMembers_founded_company_investor_type.append(BoardMembers_founded_companies['properties']['investor_type'])
                    BoardMembers_founded_company_founded_on.append(BoardMembers_founded_companies['properties']['founded_on'])
                    BoardMembers_founded_company_founded_on_trust_code.append(BoardMembers_founded_companies['properties']['founded_on_trust_code'])
                    BoardMembers_founded_company_is_closed.append(BoardMembers_founded_companies['properties']['is_closed'])
                    BoardMembers_founded_company_closed_on.append(BoardMembers_founded_companies['properties']['closed_on'])
                    BoardMembers_founded_company_closed_on_trust_code.append(BoardMembers_founded_companies['properties']['closed_on_trust_code'])
                    BoardMembers_founded_company_num_employees_min.append(BoardMembers_founded_companies['properties']['num_employees_min'])
                    BoardMembers_founded_company_num_employees_max.append(BoardMembers_founded_companies['properties']['num_employees_max'])
                    BoardMembers_founded_company_stock_exchange.append(BoardMembers_founded_companies['properties']['stock_exchange'])
                    BoardMembers_founded_company_stock_symbol.append(BoardMembers_founded_companies['properties']['stock_symbol'])
                    BoardMembers_founded_company_total_funding_usd.append(BoardMembers_founded_companies['properties']['total_funding_usd'])
                    BoardMembers_founded_company_number_of_investments.append(BoardMembers_founded_companies['properties']['number_of_investments'])
                    BoardMembers_founded_company_homepage_url.append(BoardMembers_founded_companies['properties']['homepage_url'])
                    BoardMembers_founded_company_contact_email.append(BoardMembers_founded_companies['properties']['contact_email'])
                    BoardMembers_founded_company_phone_number.append(BoardMembers_founded_companies['properties']['phone_number'])
                    BoardMembers_founded_company_rank.append(BoardMembers_founded_companies['properties']['rank'])
                    BoardMembers_founded_company_created_at.append(BoardMembers_founded_companies['properties']['created_at'])
                    BoardMembers_founded_company_updated_at.append(BoardMembers_founded_companies['properties']['updated_at'])
                 
                    # All website urls (Facebook, Twitter, and LinkedIn) for each board_members
                    BoardMembers_website_paging_total_items.append(BoardMembers_details['websites']['paging']['total_items'])
                    for BoardMembers_websites in data_board_members['data']['relationships']['websites']['items']:
                        if BoardMembers_website_paging_total_items[-1]>0: # If board_members website details are available, append the details
                            company_uuid_BoardMembers_website.append(company_details['uuid'])
                            company_name_BoardMembers_website.append(company_details['properties']['name'])
                            BoardMembers_uuid_BoardMembers_website.append(board_details['uuid'])
                            BoardMembers_first_name_BoardMembers_website.append(board_details['relationships']['person']['properties']['first_name'])
                            BoardMembers_last_name_BoardMembers_website.append(board_details['relationships']['person']['properties']['last_name'])
                            BoardMembers_website_type.append(BoardMembers_websites['type'])
                            BoardMembers_website_uuid.append(BoardMembers_websites['uuid'])
                            BoardMembers_website_website_type.append(BoardMembers_websites['properties']['website_type'])
                            BoardMembers_website_website_name.append(BoardMembers_websites['properties']['website_name'])
                            BoardMembers_website_url.append(BoardMembers_websites['properties']['url'])
                            BoardMembers_website_created_at.append(BoardMembers_websites['properties']['created_at'])
                            BoardMembers_website_updated_at.append(BoardMembers_websites['properties']['updated_at'])                    
                        else: # Else append as missing entries
                            company_uuid_BoardMembers_website.append(company_details['uuid'])
                            company_name_BoardMembers_website.append(company_details['properties']['name'])
                            BoardMembers_uuid_BoardMembers_website.append(board_details['uuid'])
                            BoardMembers_first_name_BoardMembers_website.append(board_details['relationships']['person']['properties']['first_name'])
                            BoardMembers_last_name_BoardMembers_website.append(board_details['relationships']['person']['properties']['last_name'])
                            BoardMembers_website_type.append('')
                            BoardMembers_website_uuid.append('')
                            BoardMembers_website_website_type.append('')
                            BoardMembers_website_website_name.append('')
                            BoardMembers_website_url.append('')
                            BoardMembers_website_created_at.append('')
                            BoardMembers_website_updated_at.append('')
                            
                    # All advisory roles for each board_members
                    BoardMembers_advisory_roles_paging_total_items.append(BoardMembers_details['websites']['paging']['total_items'])
                    for BoardMembers_advisory_roles in data_board_members['data']['relationships']['advisory_roles']['items']:
                        if BoardMembers_advisory_roles_paging_total_items[-1]>0: # If board_members website details are available, append the details
                            company_uuid_BoardMembers_advisory_role.append(company_details['uuid'])
                            company_name_BoardMembers_advisory_role.append(company_details['properties']['name'])
                            BoardMembers_uuid_BoardMembers_advisory_role.append(board_details['uuid'])
                            BoardMembers_first_name_BoardMembers_advisory_role.append(board_details['relationships']['person']['properties']['first_name'])
                            BoardMembers_last_name_BoardMembers_advisory_role.append(board_details['relationships']['person']['properties']['last_name'])
                            BoardMembers_advisory_role_type.append(BoardMembers_advisory_roles['type'])
                            BoardMembers_advisory_role_uuid.append(BoardMembers_advisory_roles['uuid'])
                            BoardMembers_advisory_role_title.append(BoardMembers_advisory_roles['properties']['title'])
                            BoardMembers_advisory_role_started_on.append(BoardMembers_advisory_roles['properties']['started_on'])
                            BoardMembers_advisory_role_started_on_trust_code.append(BoardMembers_advisory_roles['properties']['started_on_trust_code'])
                            BoardMembers_advisory_role_ended_on.append(BoardMembers_advisory_roles['properties']['ended_on'])
                            BoardMembers_advisory_role_ended_on_trust_code.append(BoardMembers_advisory_roles['properties']['ended_on_trust_code'])
                            BoardMembers_advisory_role_is_current.append(BoardMembers_advisory_roles['properties']['is_current'])
                            BoardMembers_advisory_role_job_type.append(BoardMembers_advisory_roles['properties']['job_type'])
                            BoardMembers_advisory_role_created_at.append(BoardMembers_advisory_roles['properties']['created_at'])
                            BoardMembers_advisory_role_updated_at.append(BoardMembers_advisory_roles['properties']['updated_at'])
                            BoardMembers_advisory_role_organization_permalink.append(BoardMembers_advisory_roles['relationships']['organization']['properties']['permalink'])
                            BoardMembers_advisory_role_organization_permalink_aliases.append(BoardMembers_advisory_roles['relationships']['organization']['properties']['permalink_aliases'])
                            BoardMembers_advisory_role_organization_api_path.append(BoardMembers_advisory_roles['relationships']['organization']['properties']['api_path'])
                            BoardMembers_advisory_role_organization_web_path.append(BoardMembers_advisory_roles['relationships']['organization']['properties']['web_path'])
                            BoardMembers_advisory_role_organization_api_url.append(BoardMembers_advisory_roles['relationships']['organization']['properties']['api_url'])
                            BoardMembers_advisory_role_organization_name.append(BoardMembers_advisory_roles['relationships']['organization']['properties']['name'])
                            BoardMembers_advisory_role_organization_also_known_as.append(BoardMembers_advisory_roles['relationships']['organization']['properties']['also_known_as'])
                            BoardMembers_advisory_role_organization_short_description.append(BoardMembers_advisory_roles['relationships']['organization']['properties']['short_description'])
                            BoardMembers_advisory_role_organization_description.append(BoardMembers_advisory_roles['relationships']['organization']['properties']['description'])
                            BoardMembers_advisory_role_organization_profile_image_url.append(BoardMembers_advisory_roles['relationships']['organization']['properties']['profile_image_url'])
                            BoardMembers_advisory_role_organization_primary_role.append(BoardMembers_advisory_roles['relationships']['organization']['properties']['primary_role'])
                            BoardMembers_advisory_role_organization_role_company.append(BoardMembers_advisory_roles['relationships']['organization']['properties']['role_company'])
                            BoardMembers_advisory_role_organization_role_investor.append(BoardMembers_advisory_roles['relationships']['organization']['properties']['role_investor'])
                            BoardMembers_advisory_role_organization_role_group.append(BoardMembers_advisory_roles['relationships']['organization']['properties']['role_group'])
                            BoardMembers_advisory_role_organization_role_school.append(BoardMembers_advisory_roles['relationships']['organization']['properties']['role_school'])
                            BoardMembers_advisory_role_organization_investor_type.append(BoardMembers_advisory_roles['relationships']['organization']['properties']['investor_type'])
                            BoardMembers_advisory_role_organization_founded_on.append(BoardMembers_advisory_roles['relationships']['organization']['properties']['founded_on'])
                            BoardMembers_advisory_role_organization_founded_on_trust_code.append(BoardMembers_advisory_roles['relationships']['organization']['properties']['founded_on_trust_code'])
                            BoardMembers_advisory_role_organization_is_closed.append(BoardMembers_advisory_roles['relationships']['organization']['properties']['is_closed'])
                            BoardMembers_advisory_role_organization_closed_on.append(BoardMembers_advisory_roles['relationships']['organization']['properties']['closed_on'])
                            BoardMembers_advisory_role_organization_closed_on_trust_code.append(BoardMembers_advisory_roles['relationships']['organization']['properties']['closed_on_trust_code'])
                            BoardMembers_advisory_role_organization_num_employees_min.append(BoardMembers_advisory_roles['relationships']['organization']['properties']['num_employees_min'])
                            BoardMembers_advisory_role_organization_num_employees_max.append(BoardMembers_advisory_roles['relationships']['organization']['properties']['num_employees_max'])
                            BoardMembers_advisory_role_organization_stock_exchange.append(BoardMembers_advisory_roles['relationships']['organization']['properties']['stock_exchange'])
                            BoardMembers_advisory_role_organization_stock_symbol.append(BoardMembers_advisory_roles['relationships']['organization']['properties']['stock_symbol'])
                            BoardMembers_advisory_role_organization_total_funding_usd.append(BoardMembers_advisory_roles['relationships']['organization']['properties']['total_funding_usd'])
                            BoardMembers_advisory_role_organization_number_of_investments.append(BoardMembers_advisory_roles['relationships']['organization']['properties']['number_of_investments'])
                            BoardMembers_advisory_role_organization_homepage_url.append(BoardMembers_advisory_roles['relationships']['organization']['properties']['homepage_url'])
                            BoardMembers_advisory_role_organization_contact_email.append(BoardMembers_advisory_roles['relationships']['organization']['properties']['contact_email'])
                            BoardMembers_advisory_role_organization_phone_number.append(BoardMembers_advisory_roles['relationships']['organization']['properties']['phone_number'])
                            BoardMembers_advisory_role_organization_rank.append(BoardMembers_advisory_roles['relationships']['organization']['properties']['rank'])
                            BoardMembers_advisory_role_organization_created_at.append(BoardMembers_advisory_roles['relationships']['organization']['properties']['created_at'])
                            BoardMembers_advisory_role_organization_updated_at.append(BoardMembers_advisory_roles['relationships']['organization']['properties']['updated_at'])
                            
                        else: # Else append as missing entries
                            company_uuid_BoardMembers_advisory_role.append(company_details['uuid'])
                            company_name_BoardMembers_advisory_role.append(company_details['properties']['name'])
                            BoardMembers_uuid_BoardMembers_advisory_role.append(board_details['uuid'])
                            BoardMembers_first_name_BoardMembers_advisory_role.append(board_details['relationships']['person']['properties']['first_name'])
                            BoardMembers_last_name_BoardMembers_advisory_role.append(board_details['relationships']['person']['properties']['last_name'])
                            BoardMembers_advisory_role_type.append('')
                            BoardMembers_advisory_role_uuid.append('')
                            BoardMembers_advisory_role_title.append('')
                            BoardMembers_advisory_role_started_on.append('')
                            BoardMembers_advisory_role_started_on_trust_code.append('')
                            BoardMembers_advisory_role_ended_on.append('')
                            BoardMembers_advisory_role_ended_on_trust_code.append('')
                            BoardMembers_advisory_role_is_current.append('')
                            BoardMembers_advisory_role_job_type.append('')
                            BoardMembers_advisory_role_created_at.append('')
                            BoardMembers_advisory_role_updated_at.append('')
                            BoardMembers_advisory_role_organization_permalink.append('')
                            BoardMembers_advisory_role_organization_permalink_aliases.append('')
                            BoardMembers_advisory_role_organization_api_path.append('')
                            BoardMembers_advisory_role_organization_web_path.append('')
                            BoardMembers_advisory_role_organization_api_url.append('')
                            BoardMembers_advisory_role_organization_name.append('')
                            BoardMembers_advisory_role_organization_also_known_as.append('')
                            BoardMembers_advisory_role_organization_short_description.append('')
                            BoardMembers_advisory_role_organization_description.append('')
                            BoardMembers_advisory_role_organization_profile_image_url.append('')
                            BoardMembers_advisory_role_organization_primary_role.append('')
                            BoardMembers_advisory_role_organization_role_company.append('')
                            BoardMembers_advisory_role_organization_role_investor.append('')
                            BoardMembers_advisory_role_organization_role_group.append('')
                            BoardMembers_advisory_role_organization_role_school.append('')
                            BoardMembers_advisory_role_organization_investor_type.append('')
                            BoardMembers_advisory_role_organization_founded_on.append('')
                            BoardMembers_advisory_role_organization_founded_on_trust_code.append('')
                            BoardMembers_advisory_role_organization_is_closed.append('')
                            BoardMembers_advisory_role_organization_closed_on.append('')
                            BoardMembers_advisory_role_organization_closed_on_trust_code.append('')
                            BoardMembers_advisory_role_organization_num_employees_min.append('')
                            BoardMembers_advisory_role_organization_num_employees_max.append('')
                            BoardMembers_advisory_role_organization_stock_exchange.append('')
                            BoardMembers_advisory_role_organization_stock_symbol.append('')
                            BoardMembers_advisory_role_organization_total_funding_usd.append('')
                            BoardMembers_advisory_role_organization_number_of_investments.append('')
                            BoardMembers_advisory_role_organization_homepage_url.append('')
                            BoardMembers_advisory_role_organization_contact_email.append('')
                            BoardMembers_advisory_role_organization_phone_number.append('')
                            BoardMembers_advisory_role_organization_rank.append('')
                            BoardMembers_advisory_role_organization_created_at.append('')
                            BoardMembers_advisory_role_organization_updated_at.append('')
                    
                    # All investments made by each board_members
                    BoardMembers_investments_paging_total_items.append(BoardMembers_details['investments']['paging']['total_items'])
                    if BoardMembers_investments_paging_total_items[-1]>0: # If board_members website details are available, append the details
                        page=1
                        while page <= funding_paging_number_of_pages: # Pagination - For any item, CrunchBase API shows at most 100 entries per page. For items with over 100 entries, we have to scrape details from each page
                            BoardMembers_investments_url = BoardMembers_details['investments']['paging']['first_page_url'] + '?page={}&sort_order=announced_on%20DESC&items_per_page=100&user_key={}'.format(page, api_key)
                            
                            try:
                                response = urllib.request.urlopen(BoardMembers_investments_url, timeout=timeout_time_seconds)
                            except:
                               #time_excep_BoardMembers_investment.append(url)
                                continue
                            data_BoardMembers_investments = json.loads(response.read().decode())
                            for BoardMembers_investments in data_BoardMembers_investments['data']['items']:
                                page = page+1
                                company_uuid_BoardMembers_investments.append(company_details['uuid'])
                                company_name_BoardMembers_investments.append(company_details['properties']['name'])
                                BoardMembers_uuid_BoardMembers_investments.append(board_details['uuid'])
                                BoardMembers_first_name_investments.append(board_details['relationships']['person']['properties']['first_name'])
                                BoardMembers_last_name_BoardMembers_investments.append(board_details['relationships']['person']['properties']['last_name'])
                                BoardMembers_investment_type.append(BoardMembers_investments['type'])
                                BoardMembers_investment_uuid.append(BoardMembers_investments['uuid'])
                                BoardMembers_investment_money_invested.append(BoardMembers_investments['properties']['money_invested'])
                                BoardMembers_investment_money_invested_currency_code.append(BoardMembers_investments['properties']['money_invested_currency_code'])
                                BoardMembers_investment_money_invested_usd.append(BoardMembers_investments['properties']['money_invested_usd'])
                                BoardMembers_investment_is_lead_investor.append(BoardMembers_investments['properties']['is_lead_investor'])
                                BoardMembers_investment_announced_on.append(BoardMembers_investments['properties']['announced_on'])
                                BoardMembers_investment_announced_on_trust_code.append(BoardMembers_investments['properties']['announced_on_trust_code'])
                                BoardMembers_investment_created_at.append(BoardMembers_investments['properties']['created_at'])
                                BoardMembers_investment_updated_at.append(BoardMembers_investments['properties']['updated_at'])
                                BoardMembers_investment_funding_round_type.append(BoardMembers_investments['relationships']['funding_round']['type'])
                                BoardMembers_investment_funding_round_uuid.append(BoardMembers_investments['relationships']['funding_round']['uuid'])
                                BoardMembers_investment_funding_round_permalink.append(BoardMembers_investments['relationships']['funding_round']['properties']['permalink'])
                                BoardMembers_investment_funding_round_api_path.append(BoardMembers_investments['relationships']['funding_round']['properties']['api_path'])
                                BoardMembers_investment_funding_round_web_path.append(BoardMembers_investments['relationships']['funding_round']['properties']['web_path'])
                                BoardMembers_investment_funding_round_api_url.append(BoardMembers_investments['relationships']['funding_round']['properties']['api_url'])
                                BoardMembers_investment_funding_round_funding_type.append(BoardMembers_investments['relationships']['funding_round']['properties']['funding_type'])
                                BoardMembers_investment_funding_round_series.append(BoardMembers_investments['relationships']['funding_round']['properties']['series'])
                                BoardMembers_investment_funding_round_series_qualifier.append(BoardMembers_investments['relationships']['funding_round']['properties']['series_qualifier'])
                                BoardMembers_investment_funding_round_announced_on.append(BoardMembers_investments['relationships']['funding_round']['properties']['announced_on'])
                                BoardMembers_investment_funding_round_announced_on_trust_code.append(BoardMembers_investments['relationships']['funding_round']['properties']['announced_on_trust_code'])
                                BoardMembers_investment_funding_round_closed_on.append(BoardMembers_investments['relationships']['funding_round']['properties']['closed_on'])
                                BoardMembers_investment_funding_round_closed_on_trust_code.append(BoardMembers_investments['relationships']['funding_round']['properties']['closed_on_trust_code'])
                                BoardMembers_investment_funding_money_raised.append(BoardMembers_investments['relationships']['funding_round']['properties']['money_raised'])
                                BoardMembers_investment_funding_round_money_raised_currency_code.append(BoardMembers_investments['relationships']['funding_round']['properties']['money_raised_currency_code'])
                                BoardMembers_investment_funding_round_money_raised_usd.append(BoardMembers_investments['relationships']['funding_round']['properties']['money_raised_usd'])
                                BoardMembers_investment_funding_round_target_money_raised.append(BoardMembers_investments['relationships']['funding_round']['properties']['target_money_raised'])
                                BoardMembers_investment_funding_round_target_money_raised_currency_code.append(BoardMembers_investments['relationships']['funding_round']['properties']['target_money_raised_currency_code'])
                                BoardMembers_investment_funding_round_target_money_raised_usd.append(BoardMembers_investments['relationships']['funding_round']['properties']['target_money_raised_usd'])
                                BoardMembers_investment_funding_round_pre_money_valuation.append(BoardMembers_investments['relationships']['funding_round']['properties']['pre_money_valuation'])
                                BoardMembers_investment_funding_round_pre_money_valuation_currency_code.append(BoardMembers_investments['relationships']['funding_round']['properties']['pre_money_valuation_currency_code'])
                                BoardMembers_investment_funding_round_pre_money_valuation_usd.append(BoardMembers_investments['relationships']['funding_round']['properties']['pre_money_valuation_usd'])
                                BoardMembers_investment_funding_round_rank.append(BoardMembers_investments['relationships']['funding_round']['properties']['rank'])
                                BoardMembers_investment_funding_round_created_at.append(BoardMembers_investments['relationships']['funding_round']['properties']['created_at'])
                                BoardMembers_investment_funding_round_updated_at.append(BoardMembers_investments['relationships']['funding_round']['properties']['updated_at'])
                                BoardMembers_investment_funding_round_funded_organization_type.append(BoardMembers_investments['relationships']['funding_round']['relationships']['funded_organization']['type'])
                                BoardMembers_investment_funding_round_funded_organization_uuid.append(BoardMembers_investments['relationships']['funding_round']['relationships']['funded_organization']['uuid'])
                                BoardMembers_investment_funding_round_funded_organization_permalink.append(BoardMembers_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['permalink'])
                                BoardMembers_investment_funding_round_funded_organization_permalink_aliases.append(BoardMembers_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['permalink_aliases'])
                                BoardMembers_investment_funding_round_funded_organization_api_path.append(BoardMembers_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['api_path'])
                                BoardMembers_investment_funding_round_funded_organization_web_path.append(BoardMembers_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['web_path'])
                                BoardMembers_investment_funding_round_funded_organization_api_url.append(BoardMembers_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['api_url'])
                                BoardMembers_investment_funding_round_funded_organization_name.append(BoardMembers_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['name'])
                                BoardMembers_investment_funding_round_funded_organization_also_known_as.append(BoardMembers_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['also_known_as'])
                                BoardMembers_investment_funding_round_funded_organization_short_description.append(BoardMembers_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['short_description'])
                                BoardMembers_investment_funding_round_funded_organization_description.append(BoardMembers_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['description'])
                                BoardMembers_investment_funding_round_funded_organization_profile_image_url.append(BoardMembers_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['profile_image_url'])
                                BoardMembers_investment_funding_round_funded_organization_primary_role.append(BoardMembers_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['primary_role'])
                                BoardMembers_investment_funding_round_funded_organization_role_company.append(BoardMembers_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['role_company'])
                                BoardMembers_investment_funding_round_funded_organization_role_investor.append(BoardMembers_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['role_investor'])
                                BoardMembers_investment_funding_round_funded_organization_role_group.append(BoardMembers_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['role_group'])
                                BoardMembers_investment_funding_round_funded_organization_role_school.append(BoardMembers_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['role_school'])
                                BoardMembers_investment_funding_round_funded_organization_investor_type.append(BoardMembers_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['investor_type'])
                                BoardMembers_investment_funding_round_funded_organization_founded_on.append(BoardMembers_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['founded_on'])
                                BoardMembers_investment_funding_round_funded_organization_founded_on_trust_code.append(BoardMembers_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['founded_on_trust_code'])
                                BoardMembers_investment_funding_round_funded_organization_is_closed.append(BoardMembers_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['is_closed'])
                                BoardMembers_investment_funding_round_funded_organization_closed_on.append(BoardMembers_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['closed_on'])
                                BoardMembers_investment_funding_round_funded_organization_closed_on_trust_code.append(BoardMembers_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['closed_on_trust_code'])
                                BoardMembers_investment_funding_round_funded_organization_num_employees_min.append(BoardMembers_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['num_employees_min'])
                                BoardMembers_investment_funding_round_funded_organization_num_employees_max.append(BoardMembers_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['num_employees_max'])
                                BoardMembers_investment_funding_round_funded_organization_stock_exchange.append(BoardMembers_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['stock_exchange'])
                                BoardMembers_investment_funding_round_funded_organization_stock_symbol.append(BoardMembers_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['stock_symbol'])
                                BoardMembers_investment_funding_round_funded_organization_total_funding_usd.append(BoardMembers_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['total_funding_usd'])
                                BoardMembers_investment_funding_round_funded_organization_number_of_investments.append(BoardMembers_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['number_of_investments'])
                                BoardMembers_investment_funding_round_funded_organization_homepage_url.append(BoardMembers_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['homepage_url'])
                                BoardMembers_investment_funding_round_funded_organization_contact_email.append(BoardMembers_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['contact_email'])
                                BoardMembers_investment_funding_round_funded_organization_phone_number.append(BoardMembers_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['phone_number'])
                                BoardMembers_investment_funding_round_funded_organization_rank.append(BoardMembers_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['rank'])
                                BoardMembers_investment_funding_round_funded_organization_created_at.append(BoardMembers_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['created_at'])
                                BoardMembers_investment_funding_round_funded_organization_updated_at.append(BoardMembers_investments['relationships']['funding_round']['relationships']['funded_organization']['properties']['updated_at'])   
        

                                
        
        
        # Re-declaring all the ouput data frames after every company is scraped
       
        Company_Details = pd.DataFrame() # Basic details for each company from company API url
        Company_FundingRounds = pd.DataFrame() # Funding details for each company from funding url for each company
        Company_FundingRounds_Investors = pd.DataFrame() # Investor details for each funding round of the company from each funding url for each company
        Company_FundingRounds_Investors_Partners =pd.DataFrame() # Partners from each investor who participated in each funding round of the company from each funding url for each company
        Company_Acquisitions = pd.DataFrame() # Acquisition (done by the company) from acquisitions url for each company
        Company_Offices = pd.DataFrame() # Office locations for each company from offices url for each company
        Company_Headquarters = pd.DataFrame() # Headquarters locations for each company from offices url for each company
        Company_SubOrganizations = pd.DataFrame() # Sub-organization details for each company from sub_organizations url for each company
        Company_Founders = pd.DataFrame() # Basic details for all founders for each company from founders url of each company
        Company_Founders_Degrees = pd.DataFrame() # Degree details for each founder of each company from each founder's url
        Company_Founders_Jobs = pd.DataFrame() # Job details for each founder of each company from each founder's url
        Company_Founders_FoundedCompanies = pd.DataFrame() # Founded companies details for each founder of each company from each founder's url
        Company_Founders_Websites = pd.DataFrame() # Website details for each founder of each company from each founder's url
        Company_Founders_AdvisoryRoles = pd.DataFrame() # Advisory role details for each founder of each company from each founder's url
        Company_Founders_Investments = pd.DataFrame() # Investment details for each investment made by each founder of each company from each founder's investment url
        Company_BoardMembers = pd.DataFrame() # Basic details for all board_members for each company from board_members url of each company
        Company_BoardMembers_Degrees = pd.DataFrame() # Degree details for each board_members of each company from each board_members's url
        Company_BoardMembers_Jobs = pd.DataFrame() # Job details for each board_members of each company from each board_members's url
        Company_BoardMembers_FoundedCompanies = pd.DataFrame() # Founded companies details for each board_members of each company from each board_members's url
        Company_BoardMembers_Websites = pd.DataFrame() # Website details for each board_members of each company from each board_members's url
        Company_BoardMembers_AdvisoryRoles = pd.DataFrame() # Advisory role details for each board_members of each company from each board_members's url
        Company_BoardMembers_Investments = pd.DataFrame() # Investment details for each investment made by each board_members of each company from each board_members's investment url
        

        
        
        Error =pd.DataFrame() #Urls for companies that returned error while scraping
        
        # Output data frame for Company/investor Details

        
        
        Company_Details['company_uuid']= company_uuid
        Company_Details['company_name']= company_name
        Company_Details['permalink']= company_permalink
        Company_Details['company_permalink_aliases']= company_permalink_aliases
        Company_Details['company_api_path']= company_api_path
        Company_Details['company_web_path']= company_web_path
        Company_Details['company_api_url']= company_api_url
        Company_Details['company_also_known_as']= company_also_known_as
        Company_Details['company_short_description']= company_short_description
        Company_Details['company_description']= company_description
        Company_Details['company_profile_image_url']= company_profile_image_url
        Company_Details['company_primary_role']= company_primary_role
        Company_Details['company_role_company']= company_role_company
        Company_Details['company_role_investor']= company_role_investor
        Company_Details['company_role_group']= company_role_group
        Company_Details['company_role_school']= company_role_school
        Company_Details['company_investor_type']= company_investor_type
        Company_Details['company_founded_on']= company_founded_on
        Company_Details['company_founded_on_trust_code']= company_founded_on_trust_code
        Company_Details['company_is_closed']= company_is_closed
        Company_Details['company_closed_on']= company_closed_on
        Company_Details['company_closed_on_trust_code']= company_closed_on_trust_code
        Company_Details['company_num_employees_min']= company_num_employees_min
        Company_Details['company_num_employees_max']= company_num_employees_max
        Company_Details['company_stock_exchange']= company_stock_exchange
        Company_Details['company_stock_symbol']= company_stock_symbol
        Company_Details['company_total_funding_usd']= company_total_funding_usd
        Company_Details['company_number_of_investments']= company_number_of_investments
        Company_Details['company_homepage_url']= company_homepage_url
        Company_Details['company_contact_email']= company_contact_email
        Company_Details['company_phone_number']= company_phone_number
        Company_Details['company_rank']= company_rank
        Company_Details['ipo_uuid']= ipo_uuid
        Company_Details['ipo_type']= ipo_type
        Company_Details['ipo_went_public_on']= ipo_went_public_on
        Company_Details['ipo_stock_exchange_symbol']= ipo_stock_exchange_symbol
        Company_Details['ipo_stock_symbol']= ipo_stock_symbol
        Company_Details['ipo_shares_sold']= ipo_shares_sold
        Company_Details['ipo_opening_share_price']= ipo_opening_share_price
        Company_Details['ipo_opening_share_price_currency_code']= ipo_opening_share_price_currency_code
        Company_Details['ipo_opening_share_price_usd']= ipo_opening_share_price_usd
        Company_Details['ipo_opening_valuation']= ipo_opening_valuation
        Company_Details['ipo_opening_valuation_currency_code']= ipo_opening_valuation_currency_code
        Company_Details['ipo_opening_valuation_usd']= ipo_opening_valuation_usd
        Company_Details['ipo_money_raised']= ipo_money_raised
        Company_Details['ipo_money_raised_currency_code']= ipo_money_raised_currency_code
        Company_Details['ipo_money_raised_usd']= ipo_money_raised_usd
        Company_Details['ipo_created_at']= ipo_created_at
        Company_Details['ipo_updated_at']= ipo_updated_at
        Company_Details['acquired_by_type']= acquired_by_type
        Company_Details['acquired_by_uuid']= acquired_by_uuid
        Company_Details['acquired_by_api_url']= acquired_by_api_url
        Company_Details['acquired_by_price']= acquired_by_price
        Company_Details['acquired_by_price_currency_code']= acquired_by_price_currency_code
        Company_Details['acquired_by_price_usd']= acquired_by_price_usd
        Company_Details['acquired_by_payment_type']= acquired_by_payment_type
        Company_Details['acquired_by_acquisition_type']= acquired_by_acquisition_type
        Company_Details['acquired_by_acquisition_status']= acquired_by_acquisition_status
        Company_Details['acquired_by_disposition_of_acquired']= acquired_by_disposition_of_acquired
        Company_Details['acquired_by_announced_on']= acquired_by_announced_on
        Company_Details['acquired_by_completed_on']= acquired_by_completed_on
        Company_Details['acquired_by_acquirer_type']= acquired_by_acquirer_type
        Company_Details['acquired_by_acquirer_uuid']= acquired_by_acquirer_uuid
        Company_Details['acquired_by_acquirer_name']= acquired_by_acquirer_name
        Company_Details['acquired_by_acquirer_also_known_as']= acquired_by_acquirer_also_known_as
        Company_Details['acquired_by_acquirer_short_description']= acquired_by_acquirer_short_description
        Company_Details['acquired_by_acquirer_description']= acquired_by_acquirer_description
        Company_Details['acquired_by_acquirer_profile_image_url']= acquired_by_acquirer_profile_image_url
        Company_Details['acquired_by_acquirer_primary_role']= acquired_by_acquirer_primary_role
        Company_Details['acquired_by_acquirer_role_company']= acquired_by_acquirer_role_company
        Company_Details['acquired_by_acquirer_role_investor']= acquired_by_acquirer_role_investor
        Company_Details['acquired_by_acquirer_role_group']= acquired_by_acquirer_role_group
        Company_Details['acquired_by_acquirer_role_school']= acquired_by_acquirer_role_school
        Company_Details['acquired_by_acquirer_investor_type']= acquired_by_acquirer_investor_type
        Company_Details['acquired_by_acquirer_founded_on']= acquired_by_acquirer_founded_on
        Company_Details['acquired_by_acquirer_is_closed']= acquired_by_acquirer_is_closed
        Company_Details['acquired_by_acquirer_closed_on']= acquired_by_acquirer_closed_on
        Company_Details['acquired_by_acquirer_num_employees_min']= acquired_by_acquirer_num_employees_min
        Company_Details['acquired_by_acquirer_num_employees_max']= acquired_by_acquirer_num_employees_max
        Company_Details['acquired_by_acquirer_stock_exchange']= acquired_by_acquirer_stock_exchange
        Company_Details['acquired_by_acquirer_stock_symbol']= acquired_by_acquirer_stock_symbol
        Company_Details['acquired_by_acquirer_total_funding_usd']= acquired_by_acquirer_total_funding_usd
        Company_Details['acquired_by_acquirer_number_of_investments']= acquired_by_acquirer_number_of_investments
        Company_Details['acquired_by_acquirer_homepage_url']= acquired_by_acquirer_homepage_url
        Company_Details['acquired_by_acquirer_contact_email']= acquired_by_acquirer_contact_email
        Company_Details['acquired_by_acquirer_phone_number']= acquired_by_acquirer_phone_number
        Company_Details['company_owned_by_paging_total_items'] = company_owned_by_paging_total_items
        Company_Details['company_owned_by_owner_type'] = company_owned_by_owner_type
        Company_Details['company_owned_by_owner_uuid'] = company_owned_by_owner_uuid
        Company_Details['company_owned_by_owner_permalink'] = company_owned_by_owner_permalink
        Company_Details['company_owned_by_owner_permalink_aliases'] = company_owned_by_owner_permalink_aliases
        Company_Details['company_owned_by_owner_api_path'] = company_owned_by_owner_api_path
        Company_Details['company_owned_by_owner_web_path'] = company_owned_by_owner_web_path
        Company_Details['company_owned_by_owner_api_url'] = company_owned_by_owner_api_url
        Company_Details['company_owned_by_owner_name'] = company_owned_by_owner_name
        Company_Details['company_owned_by_owner_also_known_as'] = company_owned_by_owner_also_known_as
        Company_Details['company_owned_by_owner_short_description'] = company_owned_by_owner_short_description
        Company_Details['company_owned_by_owner_description'] = company_owned_by_owner_description
        Company_Details['company_owned_by_owner_profile_image_url'] = company_owned_by_owner_profile_image_url
        Company_Details['company_owned_by_owner_primary_role'] = company_owned_by_owner_primary_role
        Company_Details['company_owned_by_owner_role_company'] = company_owned_by_owner_role_company
        Company_Details['company_owned_by_owner_role_investor'] = company_owned_by_owner_role_investor
        Company_Details['company_owned_by_owner_role_group'] = company_owned_by_owner_role_group
        Company_Details['company_owned_by_owner_role_school'] = company_owned_by_owner_role_school
        Company_Details['company_owned_by_owner_investor_type'] = company_owned_by_owner_investor_type
        Company_Details['company_owned_by_owner_founded_on'] = company_owned_by_owner_founded_on
        Company_Details['company_owned_by_owner_founded_on_trust_code'] = company_owned_by_owner_founded_on_trust_code
        Company_Details['company_owned_by_owner_is_closed'] = company_owned_by_owner_is_closed
        Company_Details['company_owned_by_owner_closed_on'] = company_owned_by_owner_closed_on
        Company_Details['company_owned_by_owner_closed_on_trust_code'] = company_owned_by_owner_closed_on_trust_code
        Company_Details['company_owned_by_owner_num_employees_min'] = company_owned_by_owner_num_employees_min
        Company_Details['company_owned_by_owner_num_employees_max'] = company_owned_by_owner_num_employees_max
        Company_Details['company_owned_by_owner_stock_exchange'] = company_owned_by_owner_stock_exchange
        Company_Details['company_owned_by_owner_stock_symbol'] = company_owned_by_owner_stock_symbol
        Company_Details['company_owned_by_owner_total_funding_usd'] = company_owned_by_owner_total_funding_usd
        Company_Details['company_owned_by_owner_number_of_investments'] = company_owned_by_owner_number_of_investments
        Company_Details['company_owned_by_owner_homepage_url'] = company_owned_by_owner_homepage_url
        Company_Details['company_owned_by_owner_contact_email'] = company_owned_by_owner_contact_email
        Company_Details['company_owned_by_owner_phone_number'] = company_owned_by_owner_phone_number
        Company_Details['company_owned_by_owner_rank'] = company_owned_by_owner_rank
        Company_Details['company_owned_by_owner_created_at'] = company_owned_by_owner_created_at
        Company_Details['company_owned_by_owner_updated_at'] = company_owned_by_owner_updated_at
        
        
        # Output data frame for CompanyFunding
        Company_FundingRounds['company_uuid'] = company_uuid_funding
        Company_FundingRounds['company_name']= company_name_funding
        Company_FundingRounds['funding_type']= funding_type
        Company_FundingRounds['funding_uuid']= funding_uuid
        Company_FundingRounds['funding_permalink'] = funding_permalink
        Company_FundingRounds['funding_web_path'] = funding_web_path
        Company_FundingRounds['funding_api_url'] = funding_api_url
        Company_FundingRounds['funding_funding_type'] = funding_funding_type
        Company_FundingRounds['funding_series'] = funding_series
        Company_FundingRounds['funding_series_qualifier'] = funding_series_qualifier
        Company_FundingRounds['funding_announced_on'] = funding_announced_on
        Company_FundingRounds['funding_announced_on_trust_code'] = funding_announced_on_trust_code
        Company_FundingRounds['funding_closed_on'] = funding_closed_on
        Company_FundingRounds['funding_closed_on_trust_code'] = funding_closed_on_trust_code
        Company_FundingRounds['funding_funding_money_raised'] = funding_funding_money_raised
        Company_FundingRounds['funding_money_raised_currency_code'] = funding_money_raised_currency_code
        Company_FundingRounds['funding_money_raised_usd'] = funding_money_raised_usd
        Company_FundingRounds['funding_target_money_raised'] = funding_target_money_raised
        Company_FundingRounds['funding_target_money_raised_currency_code'] = funding_target_money_raised_currency_code
        Company_FundingRounds['funding_target_money_raised_usd'] = funding_target_money_raised_usd
        Company_FundingRounds['funding_pre_money_valuation'] = funding_pre_money_valuation
        Company_FundingRounds['funding_pre_money_valuation_currency_code'] = funding_pre_money_valuation_currency_code
        Company_FundingRounds['funding_pre_money_valuation_usd'] = funding_pre_money_valuation_usd
        Company_FundingRounds['funding_rank'] = funding_rank
        Company_FundingRounds['funding_created_at'] = funding_created_at
        Company_FundingRounds['funding_updated_at'] = funding_updated_at
        
        # Output data frame for all investors in each funding round
        Company_FundingRounds_Investors['company_uuid'] = company_uuid_funding_investor
        Company_FundingRounds_Investors['company_name'] = company_name_funding_investor
        Company_FundingRounds_Investors['funding_type'] = funding_type_funding_investor
        Company_FundingRounds_Investors['funding_uuid'] = funding_uuid_funding_investor
        Company_FundingRounds_Investors['funding_investor_type'] = funding_investor_type
        Company_FundingRounds_Investors['funding_investor_uuid'] = funding_investor_uuid
        Company_FundingRounds_Investors['funding_investor_permalink'] = funding_investor_permalink
        Company_FundingRounds_Investors['funding_investor_permalink_aliases'] = funding_investor_permalink_aliases
        Company_FundingRounds_Investors['funding_investor_api_path'] = funding_investor_api_path
        Company_FundingRounds_Investors['funding_investor_web_path'] = funding_investor_web_path
        Company_FundingRounds_Investors['funding_investor_api_url'] = funding_investor_api_url
        Company_FundingRounds_Investors['funding_investor_name'] = funding_investor_name
        Company_FundingRounds_Investors['funding_investor_also_known_as'] = funding_investor_also_known_as
        Company_FundingRounds_Investors['funding_investor_short_description'] = funding_investor_short_description
        Company_FundingRounds_Investors['funding_investor_description'] = funding_investor_description
        Company_FundingRounds_Investors['funding_investor_profile_image_url'] = funding_investor_profile_image_url
        Company_FundingRounds_Investors['funding_investor_primary_role'] = funding_investor_primary_role
        Company_FundingRounds_Investors['funding_investor_role_company'] = funding_investor_role_company
        Company_FundingRounds_Investors['funding_investor_role_investor'] = funding_investor_role_investor
        Company_FundingRounds_Investors['funding_investor_role_group'] = funding_investor_role_group
        Company_FundingRounds_Investors['funding_investor_role_school'] = funding_investor_role_school
        Company_FundingRounds_Investors['funding_investor_investor_type'] = funding_investor_investor_type
        Company_FundingRounds_Investors['funding_investor_founded_on'] = funding_investor_founded_on
        Company_FundingRounds_Investors['funding_investor_founded_on_trust_code'] = funding_investor_founded_on_trust_code
        Company_FundingRounds_Investors['funding_investor_is_closed'] = funding_investor_is_closed
        Company_FundingRounds_Investors['funding_investor_closed_on'] = funding_investor_closed_on
        Company_FundingRounds_Investors['funding_investor_closed_on_trust_code'] = funding_investor_closed_on_trust_code
        Company_FundingRounds_Investors['funding_investor_num_employees_min'] = funding_investor_num_employees_min
        Company_FundingRounds_Investors['funding_investor_num_employees_max'] = funding_investor_num_employees_max
        Company_FundingRounds_Investors['funding_investor_stock_exchange'] = funding_investor_stock_exchange
        Company_FundingRounds_Investors['funding_investor_stock_symbol'] = funding_investor_stock_symbol
        Company_FundingRounds_Investors['funding_investor_total_funding_usd'] = funding_investor_total_funding_usd
        Company_FundingRounds_Investors['funding_investor_number_of_investments'] = funding_investor_number_of_investments
        Company_FundingRounds_Investors['funding_investor_homepage_url'] = funding_investor_homepage_url
        Company_FundingRounds_Investors['funding_investor_contact_email'] = funding_investor_contact_email
        Company_FundingRounds_Investors['funding_investor_phone_number'] = funding_investor_phone_number
        Company_FundingRounds_Investors['funding_investor_rank'] = funding_investor_rank
        Company_FundingRounds_Investors['funding_investor_created_at'] = funding_investor_created_at
        Company_FundingRounds_Investors['funding_investor_updated_at'] = funding_investor_updated_at
        Company_FundingRounds_Investors['funding_permalink'] = funding_permalink_funding_investor
        Company_FundingRounds_Investors['funding_api_path'] = funding_api_path_funding_investor
        Company_FundingRounds_Investors['funding_web_path'] = funding_web_path_funding_investor
        Company_FundingRounds_Investors['funding_api_url'] = funding_api_url_funding_investor
        Company_FundingRounds_Investors['funding_funding'] = funding_funding_type_funding_investor
        Company_FundingRounds_Investors['funding_series'] = funding_series_funding_investor
        Company_FundingRounds_Investors['funding_series_qualifier'] = funding_series_qualifier_funding_investor
        Company_FundingRounds_Investors['funding_announced_on'] = funding_announced_on_funding_investor
        Company_FundingRounds_Investors['funding_announced_on_trust_code'] = funding_announced_on_trust_code_funding_investor
        Company_FundingRounds_Investors['funding_closed_on'] = funding_closed_on_funding_investor
        Company_FundingRounds_Investors['funding_closed_on_trust_code'] = funding_closed_on_trust_code_funding_investor
        Company_FundingRounds_Investors['funding_funding_money_raised'] = funding_funding_money_raised_funding_investor
        Company_FundingRounds_Investors['funding_money_raised_currency_code'] = funding_money_raised_currency_code_funding_investor
        Company_FundingRounds_Investors['funding_money_raised_usd'] = funding_money_raised_usd_funding_investor
        Company_FundingRounds_Investors['funding_target_money_raised_funding_investor'] = funding_target_money_raised_funding_investor
        Company_FundingRounds_Investors['funding_target_money_raised_currency_code'] = funding_target_money_raised_currency_code_funding_investor
        Company_FundingRounds_Investors['funding_target_money_raised_usd'] = funding_target_money_raised_usd_funding_investor
        Company_FundingRounds_Investors['funding_pre_money_valuation'] = funding_pre_money_valuation_funding_investor
        Company_FundingRounds_Investors['funding_pre_money_valuation_currency_code'] = funding_pre_money_valuation_currency_code_funding_investor
        Company_FundingRounds_Investors['funding_pre_money_valuation_usd'] = funding_pre_money_valuation_usd_funding_investor
        Company_FundingRounds_Investors['funding_rank'] = funding_rank_funding_investor
        Company_FundingRounds_Investors['funding_created_at'] = funding_created_at_funding_investor
        Company_FundingRounds_Investors['funding_updated_at'] = funding_updated_at_funding_investor
        Company_FundingRounds_Investors['funding_investor_first_name'] = funding_investor_first_name
        Company_FundingRounds_Investors['funding_investor_last_name'] = funding_investor_last_name
        Company_FundingRounds_Investors['funding_investor_gender'] = funding_investor_gender
        Company_FundingRounds_Investors['funding_investor_bio'] = funding_investor_bio
        Company_FundingRounds_Investors['funding_investor_born_on'] = funding_investor_born_on
        Company_FundingRounds_Investors['funding_investor_born_on_trust_code'] = funding_investor_born_on_trust_code
        Company_FundingRounds_Investors['funding_investor_died_on'] = funding_investor_died_on
        Company_FundingRounds_Investors['funding_investor_died_on_trust_code'] = funding_investor_died_on_trust_code
        Company_FundingRounds_Investors['funding_investor_money_invested'] = funding_investor_money_invested
        Company_FundingRounds_Investors['funding_investor_money_invested_currency_code'] = funding_investor_money_invested_currency_code
        Company_FundingRounds_Investors['funding_investor_money_invested_usd'] = funding_investor_money_invested_usd
        Company_FundingRounds_Investors['funding_investor_is_lead_investor'] = funding_investor_is_lead_investor
        
        
        Company_FundingRounds_Investors_Partners['company_uuid'] = company_uuid_funding_investor_partner
        Company_FundingRounds_Investors_Partners['company_name'] = company_name_funding_investor_partner
        Company_FundingRounds_Investors_Partners['funding_type'] = funding_type_funding_investor_partner
        Company_FundingRounds_Investors_Partners['funding_uuid'] = funding_uuid_funding_investor_partner
        Company_FundingRounds_Investors_Partners['funding_funding_type'] = funding_funding_type_funding_investor_partner
        Company_FundingRounds_Investors_Partners['funding_series'] = funding_series_funding_investor_partner
        Company_FundingRounds_Investors_Partners['funding_announced_on'] = funding_announced_on_funding_investor_partner
        Company_FundingRounds_Investors_Partners['funding_investor_uuid'] = funding_investor_uuid_investor_partner    
        Company_FundingRounds_Investors_Partners['funding_investor_partner_type'] = funding_investor_partner_type
        Company_FundingRounds_Investors_Partners['funding_investor_partner_uuid'] = funding_investor_partner_uuid
        Company_FundingRounds_Investors_Partners['funding_investor_partner_permalink'] = funding_investor_partner_permalink
        Company_FundingRounds_Investors_Partners['funding_investor_partner_permalink_aliases'] = funding_investor_partner_permalink_aliases
        Company_FundingRounds_Investors_Partners['funding_investor_partner_api_path'] = funding_investor_partner_api_path
        Company_FundingRounds_Investors_Partners['funding_investor_partner_web_path'] = funding_investor_partner_web_path
        Company_FundingRounds_Investors_Partners['funding_investor_partner_api_url'] = funding_investor_partner_api_url
        Company_FundingRounds_Investors_Partners['funding_investor_partner_first_name'] = funding_investor_partner_first_name
        Company_FundingRounds_Investors_Partners['funding_investor_partner_last_name'] = funding_investor_partner_last_name
        Company_FundingRounds_Investors_Partners['funding_investor_partner_gender'] = funding_investor_partner_gender
        Company_FundingRounds_Investors_Partners['funding_investor_partner_also_known_as'] = funding_investor_partner_also_known_as
        Company_FundingRounds_Investors_Partners['funding_investor_partner_bio'] = funding_investor_partner_bio
        Company_FundingRounds_Investors_Partners['funding_investor_partner_profile_image_url'] = funding_investor_partner_profile_image_url
        Company_FundingRounds_Investors_Partners['funding_investor_partner_role_investor'] = funding_investor_partner_role_investor
        Company_FundingRounds_Investors_Partners['funding_investor_partner_born_on'] = funding_investor_partner_born_on
        Company_FundingRounds_Investors_Partners['funding_investor_partner_born_on_trust_code'] = funding_investor_partner_born_on_trust_code
        Company_FundingRounds_Investors_Partners['funding_investor_partner_died_on'] = funding_investor_partner_died_on
        Company_FundingRounds_Investors_Partners['funding_investor_partner_died_on_trust_code'] = funding_investor_partner_died_on_trust_code
        Company_FundingRounds_Investors_Partners['funding_investor_partner_rank'] = funding_investor_partner_rank
        Company_FundingRounds_Investors_Partners['funding_investor_partner_created_at'] = funding_investor_partner_created_at
        Company_FundingRounds_Investors_Partners['funding_investor_partner_updated_at'] = funding_investor_partner_updated_at
        
        
        # Output data frame for CompanyAcquisitions
        Company_Acquisitions['company_uuid'] = company_uuid_acquisition
        Company_Acquisitions['company_name'] = company_name_acquisition
        Company_Acquisitions['acquisition_type'] = acquisition_type
        Company_Acquisitions['acquisition_uuid'] = acquisition_uuid
        Company_Acquisitions['acquisition_announced_on'] = acquisition_announced_on
        Company_Acquisitions['acquisition_permalink'] = acquisition_permalink
        Company_Acquisitions['acquisition_api_path'] = acquisition_api_path
        Company_Acquisitions['acquisition_web_path'] = acquisition_web_path
        Company_Acquisitions['acquisition_api_url'] = acquisition_api_url
        Company_Acquisitions['acquisition_price'] = acquisition_price
        Company_Acquisitions['acquisition_price_currency_code'] = acquisition_price_currency_code
        Company_Acquisitions['acquisition_price_usd'] = acquisition_price_usd
        Company_Acquisitions['acquisition_payment_type'] = acquisition_payment_type
        Company_Acquisitions['acquisition_acquisition_type'] = acquisition_acquisition_type
        Company_Acquisitions['acquisition_acquisition_status'] = acquisition_acquisition_status
        Company_Acquisitions['acquisition_disposition_of_acquired'] = acquisition_disposition_of_acquired
        Company_Acquisitions['acquisition_announced_on'] = acquisition_announced_on
        Company_Acquisitions['acquisition_announced_on_trust_code'] = acquisition_announced_on_trust_code
        Company_Acquisitions['acquisition_completed_on'] = acquisition_completed_on
        Company_Acquisitions['acquisition_completed_on_trust_code'] = acquisition_completed_on_trust_code
        Company_Acquisitions['acquisition_rank'] = acquisition_rank
        Company_Acquisitions['acquisition_created_at'] = acquisition_created_at
        Company_Acquisitions['acquisition_updated_at'] = acquisition_updated_at
        Company_Acquisitions['target_type'] = target_type
        Company_Acquisitions['target_uuid'] = target_uuid
        Company_Acquisitions['target_permalink'] = target_permalink
        Company_Acquisitions['target_permalink_aliases'] = target_permalink_aliases
        Company_Acquisitions['target_api_path'] = target_api_path
        Company_Acquisitions['target_web_path'] = target_web_path
        Company_Acquisitions['target_api_url'] = target_api_url
        Company_Acquisitions['target_name'] = target_name
        Company_Acquisitions['target_also_known_as'] = target_also_known_as
        Company_Acquisitions['target_short_description'] = target_short_description
        Company_Acquisitions['target_description'] = target_description
        Company_Acquisitions['target_profile_image_url'] = target_profile_image_url
        Company_Acquisitions['target_primary_role'] = target_primary_role
        Company_Acquisitions['target_role_company'] = target_role_company
        Company_Acquisitions['target_role_investor'] = target_role_investor
        Company_Acquisitions['target_role_group'] = target_role_group
        Company_Acquisitions['target_role_school'] = target_role_school
        Company_Acquisitions['target_investor_type'] = target_investor_type
        Company_Acquisitions['target_founded_on'] = target_founded_on
        Company_Acquisitions['target_founded_on_trust_code'] = target_founded_on_trust_code
        Company_Acquisitions['target_is_closed'] = target_is_closed
        Company_Acquisitions['target_closed_on'] = target_closed_on
        Company_Acquisitions['target_closed_on_trust_code'] = target_closed_on_trust_code
        Company_Acquisitions['target_num_employees_min'] = target_num_employees_min
        Company_Acquisitions['target_num_employees_max'] = target_num_employees_max
        Company_Acquisitions['target_stock_exchange'] = target_stock_exchange
        Company_Acquisitions['target_stock_symbol'] = target_stock_symbol
        Company_Acquisitions['target_total_funding_usd'] = target_total_funding_usd
        Company_Acquisitions['target_number_of_investments'] = target_number_of_investments
        Company_Acquisitions['target_homepage_url'] = target_homepage_url
        Company_Acquisitions['target_contact_email'] = target_contact_email
        Company_Acquisitions['target_phone_number'] = target_phone_number
        Company_Acquisitions['target_rank'] = target_rank
        Company_Acquisitions['target_created_at'] = target_created_at
        Company_Acquisitions['target_updated_at'] = target_updated_at
        
        Company_Offices['company_uuid'] = company_uuid_offices
        Company_Offices['company_name'] = company_name_offices
        Company_Offices['company_office_type'] = company_office_type
        Company_Offices['company_office_uuid'] = company_office_uuid
        Company_Offices['company_office_street_1'] = company_office_street_1
        Company_Offices['company_office_street_2'] = company_office_street_2
        Company_Offices['company_office_postal_code'] = company_office_postal_code
        Company_Offices['company_office_city'] = company_office_city
        Company_Offices['company_office_region'] = company_office_region
        Company_Offices['company_office_country'] = company_office_country
        Company_Offices['company_office_city_web_path'] = company_office_city_web_path
        Company_Offices['company_office_region_code2'] = company_office_region_code2
        Company_Offices['company_office_region_web_path'] = company_office_region_web_path
        Company_Offices['company_office_country_code2'] = company_office_country_code2
        Company_Offices['company_office_country_code3'] = company_office_country_code3
        Company_Offices['company_office_country_web_path'] = company_office_country_web_path
        Company_Offices['company_office_latitude'] = company_office_latitude
        Company_Offices['company_office_longitude'] = company_office_longitude
        Company_Offices['company_office_created_at'] = company_office_created_at
        Company_Offices['company_office_updated_at'] = company_office_updated_at
        Company_Offices['company_offices_total_items'] = company_offices_total_items
        
        Company_Headquarters['company_uuid'] = company_uuid_headquarters
        Company_Headquarters['company_name'] = company_name_headquarters
        Company_Headquarters['company_headquarters_type'] = company_headquarters_type
        Company_Headquarters['company_headquarters_uuid'] = company_headquarters_uuid
        Company_Headquarters['company_headquarters_name'] = company_headquarters_name
        Company_Headquarters['company_headquarters_street_1'] = company_headquarters_street_1
        Company_Headquarters['company_headquarters_street_2'] = company_headquarters_street_2
        Company_Headquarters['company_headquarters_postal_code'] = company_headquarters_postal_code
        Company_Headquarters['company_headquarters_city'] = company_headquarters_city
        Company_Headquarters['company_headquarters_region'] = company_headquarters_region
        Company_Headquarters['company_headquarters_country'] = company_headquarters_country
        Company_Headquarters['company_headquarters_city_web_path'] = company_headquarters_city_web_path
        Company_Headquarters['company_headquarters_region_code2'] = company_headquarters_region_code2
        Company_Headquarters['company_headquarters_region_web_path'] = company_headquarters_region_web_path
        Company_Headquarters['company_headquarters_country_code2'] = company_headquarters_country_code2
        Company_Headquarters['company_headquarters_country_code3'] = company_headquarters_country_code3
        Company_Headquarters['company_headquarters_country_web_path'] = company_headquarters_country_web_path
        Company_Headquarters['company_headquarters_latitude'] = company_headquarters_latitude
        Company_Headquarters['company_headquarters_longitude'] = company_headquarters_longitude
        Company_Headquarters['company_headquarters_created_at'] = company_headquarters_created_at
        Company_Headquarters['company_headquarters_updated_at'] = company_headquarters_updated_at
        
        # Output data frame for CompanySubOrganizations
        Company_SubOrganizations['company_uuid'] = company_uuid_sub_organizations
        Company_SubOrganizations['company_name'] = company_name_sub_organizations
        Company_SubOrganizations['sub_organization_type'] = sub_organization_type
        Company_SubOrganizations['sub_organization_uuid'] = sub_organization_uuid
        Company_SubOrganizations['sub_organization_permalink'] = sub_organization_permalink
        Company_SubOrganizations['sub_organization_permalink_aliases'] = sub_organization_permalink_aliases
        Company_SubOrganizations['sub_organization_api_path'] = sub_organization_api_path
        Company_SubOrganizations['sub_organization_web_path'] = sub_organization_web_path
        Company_SubOrganizations['sub_organization_api_url'] = sub_organization_api_url
        Company_SubOrganizations['sub_organization_name'] = sub_organization_name
        Company_SubOrganizations['sub_organization_also_known_as'] = sub_organization_also_known_as
        Company_SubOrganizations['sub_organization_short_description'] = sub_organization_short_description
        Company_SubOrganizations['sub_organization_description'] = sub_organization_description
        Company_SubOrganizations['sub_organization_profile_image_url'] = sub_organization_profile_image_url
        Company_SubOrganizations['sub_organization_primary_role'] = sub_organization_primary_role
        Company_SubOrganizations['sub_organization_role_company'] = sub_organization_role_company
        Company_SubOrganizations['sub_organization_role_investor'] = sub_organization_role_investor
        Company_SubOrganizations['sub_organization_role_group'] = sub_organization_role_group
        Company_SubOrganizations['sub_organization_role_school'] = sub_organization_role_school
        Company_SubOrganizations['sub_organization_investor_type'] = sub_organization_investor_type
        Company_SubOrganizations['sub_organization_founded_on'] = sub_organization_founded_on
        Company_SubOrganizations['sub_organization_founded_on_trust_code'] = sub_organization_founded_on_trust_code
        Company_SubOrganizations['sub_organization_is_closed'] = sub_organization_is_closed
        Company_SubOrganizations['sub_organization_closed_on']  = sub_organization_closed_on
        Company_SubOrganizations['sub_organization_closed_on_trust_code'] = sub_organization_closed_on_trust_code
        Company_SubOrganizations['sub_organization_num_employees_min'] = sub_organization_num_employees_min
        Company_SubOrganizations['sub_organization_num_employees_max'] = sub_organization_num_employees_max
        Company_SubOrganizations['sub_organization_stock_exchange'] = sub_organization_stock_exchange
        Company_SubOrganizations['sub_organization_stock_symbol'] = sub_organization_stock_symbol
        Company_SubOrganizations['sub_organization_total_funding_usd'] = sub_organization_total_funding_usd
        Company_SubOrganizations['sub_organization_number_of_investments'] = sub_organization_number_of_investments
        Company_SubOrganizations['sub_organization_homepage_url'] = sub_organization_homepage_url
        Company_SubOrganizations['sub_organization_contact_email'] = sub_organization_contact_email
        Company_SubOrganizations['sub_organization_phone_number'] = sub_organization_phone_number
        Company_SubOrganizations['sub_organization_rank'] = sub_organization_rank
        Company_SubOrganizations['sub_organization_created_at'] = sub_organization_created_at
        Company_SubOrganizations['sub_organization_updated_at'] = sub_organization_updated_at
        
        # Output data frame for CompanyFounders
        Company_Founders['company_uuid'] = company_uuid_founder
        Company_Founders['company_name'] = company_name_founder
        Company_Founders['founder_type'] = founder_type
        Company_Founders['founder_uuid'] = founder_uuid
        Company_Founders['founder_permalink'] = founder_permalink
        Company_Founders['founder_api_path'] = founder_api_path
        Company_Founders['founder_web_path'] = founder_web_path
        Company_Founders['founder_api_url'] = founder_api_url
        Company_Founders['founder_first_name'] = founder_first_name
        Company_Founders['founder_last_name'] = founder_last_name
        Company_Founders['founder_gender'] = founder_gender
        Company_Founders['founder_also_known_as'] = founder_also_known_as
        Company_Founders['founder_bio'] = founder_bio
        Company_Founders['founder_profile_image_url'] = founder_profile_image_url
        Company_Founders['founder_role_investor'] = founder_role_investor
        Company_Founders['founder_born_on'] = founder_born_on
        Company_Founders['founder_born_on_trust_code'] = founder_born_on_trust_code
        Company_Founders['founder_died_on'] = founder_died_on
        Company_Founders['founder_died_on_trust_code'] = founder_died_on_trust_code
        Company_Founders['founder_rank'] = founder_rank
        Company_Founders['founder_created_at'] = founder_created_at
        Company_Founders['founder_updated_at'] = founder_updated_at
        Company_Founders['founder_primary_location_type'] = founder_primary_location_type
        Company_Founders['founder_primary_location_uuid'] = founder_primary_location_uuid
        Company_Founders['founder_primary_location_uuid'] = founder_primary_location_uuid
        Company_Founders['founder_primary_location_location_type'] = founder_primary_location_location_type
        Company_Founders['founder_primary_location_parent_location_uuid'] = founder_primary_location_parent_location_uuid
        Company_Founders['founder_primary_location_city'] = founder_primary_location_city
        Company_Founders['founder_primary_location_region'] = founder_primary_location_region
        Company_Founders['founder_primary_location_region_code2'] = founder_primary_location_region_code2
        Company_Founders['founder_primary_location_country'] = founder_primary_location_country
        Company_Founders['founder_primary_location_country_code2'] = founder_primary_location_country_code2
        Company_Founders['founder_primary_location_country_code3'] = founder_primary_location_country_code3
        Company_Founders['founder_primary_location_continent'] = founder_primary_location_continent
        Company_Founders['founder_primary_location_created_at'] = founder_primary_location_created_at
        Company_Founders['founder_primary_location_updated_at'] = founder_primary_location_updated_at
        Company_Founders['founder_primary_affiliation_type'] = founder_primary_affiliation_type
        Company_Founders['founder_primary_affiliation_uuid'] = founder_primary_affiliation_uuid
        Company_Founders['founder_primary_affiliation_title'] = founder_primary_affiliation_title
        Company_Founders['founder_primary_affiliation_started_on'] = founder_primary_affiliation_started_on
        Company_Founders['founder_primary_affiliation_started_on_trust_code'] = founder_primary_affiliation_started_on_trust_code
        Company_Founders['founder_primary_affiliation_ended_on'] = founder_primary_affiliation_ended_on
        Company_Founders['founder_primary_affiliation_ended_on_trust_code'] = founder_primary_affiliation_ended_on_trust_code   
        Company_Founders['founder_primary_affiliation_is_current'] = founder_primary_affiliation_is_current
        Company_Founders['founder_primary_affiliation_job_type'] = founder_primary_affiliation_job_type
        Company_Founders['founder_primary_affiliation_created_at'] = founder_primary_affiliation_created_at
        Company_Founders['founder_primary_affiliation_updated_at'] = founder_primary_affiliation_updated_at
        Company_Founders['founder_primary_affiliation_organization_type'] = founder_primary_affiliation_organization_type
        Company_Founders['founder_primary_affiliation_organization_uuid'] = founder_primary_affiliation_organization_uuid
        Company_Founders['founder_primary_affiliation_organization_permalink'] = founder_primary_affiliation_organization_permalink
        Company_Founders['founder_primary_affiliation_organization_permalink_aliases'] = founder_primary_affiliation_organization_permalink_aliases
        Company_Founders['founder_primary_affiliation_organization_api_path'] = founder_primary_affiliation_organization_api_path
        Company_Founders['founder_primary_affiliation_organization_web_path'] = founder_primary_affiliation_organization_web_path
        Company_Founders['founder_primary_affiliation_organization_api_url'] = founder_primary_affiliation_organization_api_url
        Company_Founders['founder_primary_affiliation_organization_name'] = founder_primary_affiliation_organization_name
        Company_Founders['founder_primary_affiliation_organization_also_known_as'] = founder_primary_affiliation_organization_also_known_as
        Company_Founders['founder_primary_affiliation_organization_short_description'] = founder_primary_affiliation_organization_short_description
        Company_Founders['founder_primary_affiliation_organization_description'] = founder_primary_affiliation_organization_description
        Company_Founders['founder_primary_affiliation_organization_profile_image_url'] = founder_primary_affiliation_organization_profile_image_url
        Company_Founders['founder_primary_affiliation_organization_primary_role'] = founder_primary_affiliation_organization_primary_role
        Company_Founders['founder_primary_affiliation_organization_role_company'] = founder_primary_affiliation_organization_role_company
        Company_Founders['founder_primary_affiliation_organization_role_investor'] = founder_primary_affiliation_organization_role_investor
        Company_Founders['founder_primary_affiliation_organization_role_group'] = founder_primary_affiliation_organization_role_group
        Company_Founders['founder_primary_affiliation_organization_role_school'] = founder_primary_affiliation_organization_role_school
        Company_Founders['founder_primary_affiliation_organization_investor_type'] = founder_primary_affiliation_organization_investor_type
        Company_Founders['founder_primary_affiliation_organization_founded_on'] = founder_primary_affiliation_organization_founded_on
        Company_Founders['founder_primary_affiliation_organization_founded_on_trust_code'] = founder_primary_affiliation_organization_founded_on_trust_code
        Company_Founders['founder_primary_affiliation_organization_is_closed'] = founder_primary_affiliation_organization_is_closed
        Company_Founders['founder_primary_affiliation_organization_closed_on'] = founder_primary_affiliation_organization_closed_on
        Company_Founders['founder_primary_affiliation_organization_closed_on_trust_code'] = founder_primary_affiliation_organization_closed_on_trust_code
        Company_Founders['founder_primary_affiliation_organization_num_employees_min'] = founder_primary_affiliation_organization_num_employees_min
        Company_Founders['founder_primary_affiliation_organization_num_employees_max'] = founder_primary_affiliation_organization_num_employees_max
        Company_Founders['founder_primary_affiliation_organization_stock_exchange'] = founder_primary_affiliation_organization_stock_exchange
        Company_Founders['founder_primary_affiliation_organization_stock_symbol'] = founder_primary_affiliation_organization_stock_symbol
        Company_Founders['founder_primary_affiliation_organization_total_funding_usd'] = founder_primary_affiliation_organization_total_funding_usd
        Company_Founders['founder_primary_affiliation_organization_number_of_investments'] = founder_primary_affiliation_organization_number_of_investments
        Company_Founders['founder_primary_affiliation_organization_homepage_url'] = founder_primary_affiliation_organization_homepage_url
        Company_Founders['founder_primary_affiliation_organization_contact_email'] = founder_primary_affiliation_organization_contact_email
        Company_Founders['founder_primary_affiliation_organization_phone_number'] = founder_primary_affiliation_organization_phone_number
        Company_Founders['founder_primary_affiliation_organization_rank'] = founder_primary_affiliation_organization_rank
        Company_Founders['founder_primary_affiliation_organization_created_at'] = founder_primary_affiliation_organization_created_at
        Company_Founders['founder_primary_affiliation_organization_updated_at'] = founder_primary_affiliation_organization_updated_at
        Company_Founders['founder_primary_image_type'] = founder_primary_image_type
        Company_Founders['founder_primary_image_uuid'] = founder_primary_image_uuid
        Company_Founders['founder_primary_image_asset_path'] = founder_primary_image_asset_path
        Company_Founders['founder_primary_image_asset_url'] = founder_primary_image_asset_url
        Company_Founders['founder_primary_image_content_type'] = founder_primary_image_content_type
        Company_Founders['founder_primary_image_height'] = founder_primary_image_height
        Company_Founders['founder_primary_image_width'] = founder_primary_image_width
        Company_Founders['founder_primary_image_filesize'] = founder_primary_image_filesize
        Company_Founders['founder_primary_image_created_at'] = founder_primary_image_created_at
        Company_Founders['founder_primary_image_updated_at'] = founder_primary_image_updated_at
        Company_Founders['founder_primary_location_type'] = founder_primary_location_type
        Company_Founders['founder_primary_location_uuid'] = founder_primary_location_uuid
        Company_Founders['founder_primary_location_uuid'] = founder_primary_location_uuid
        Company_Founders['founder_primary_location_location_type'] = founder_primary_location_location_type
        Company_Founders['founder_primary_location_parent_location_uuid'] = founder_primary_location_parent_location_uuid
        Company_Founders['founder_primary_location_city'] = founder_primary_location_city
        Company_Founders['founder_primary_location_region'] = founder_primary_location_region
        Company_Founders['founder_primary_location_region_code2'] = founder_primary_location_region_code2
        Company_Founders['founder_primary_location_country'] = founder_primary_location_country
        Company_Founders['founder_primary_location_country_code2'] = founder_primary_location_country_code2
        Company_Founders['founder_primary_location_country_code3'] = founder_primary_location_country_code3
        Company_Founders['founder_primary_location_continent'] = founder_primary_location_continent
        Company_Founders['founder_primary_location_created_at'] = founder_primary_location_created_at
        Company_Founders['founder_primary_location_updated_at'] = founder_primary_location_updated_at
        Company_Founders['founder_primary_affiliation_type'] = founder_primary_affiliation_type
        Company_Founders['founder_primary_affiliation_uuid'] = founder_primary_affiliation_uuid
        Company_Founders['founder_primary_affiliation_title'] = founder_primary_affiliation_title
        Company_Founders['founder_primary_affiliation_started_on'] = founder_primary_affiliation_started_on
        Company_Founders['founder_primary_affiliation_started_on_trust_code'] = founder_primary_affiliation_started_on_trust_code
        Company_Founders['founder_primary_affiliation_ended_on'] = founder_primary_affiliation_ended_on
        Company_Founders['founder_primary_affiliation_ended_on_trust_code'] = founder_primary_affiliation_ended_on_trust_code   
        Company_Founders['founder_primary_affiliation_is_current'] = founder_primary_affiliation_is_current
        Company_Founders['founder_primary_affiliation_job_type'] = founder_primary_affiliation_job_type
        Company_Founders['founder_primary_affiliation_created_at'] = founder_primary_affiliation_created_at
        Company_Founders['founder_primary_affiliation_updated_at'] = founder_primary_affiliation_updated_at
        Company_Founders['founder_primary_affiliation_organization_type'] = founder_primary_affiliation_organization_type
        Company_Founders['founder_primary_affiliation_organization_uuid'] = founder_primary_affiliation_organization_uuid
        Company_Founders['founder_primary_affiliation_organization_permalink'] = founder_primary_affiliation_organization_permalink
        Company_Founders['founder_primary_affiliation_organization_permalink_aliases'] = founder_primary_affiliation_organization_permalink_aliases
        Company_Founders['founder_primary_affiliation_organization_api_path'] = founder_primary_affiliation_organization_api_path
        Company_Founders['founder_primary_affiliation_organization_web_path'] = founder_primary_affiliation_organization_web_path
        Company_Founders['founder_primary_affiliation_organization_api_url'] = founder_primary_affiliation_organization_api_url
        Company_Founders['founder_primary_affiliation_organization_name'] = founder_primary_affiliation_organization_name
        Company_Founders['founder_primary_affiliation_organization_also_known_as'] = founder_primary_affiliation_organization_also_known_as
        Company_Founders['founder_primary_affiliation_organization_short_description'] = founder_primary_affiliation_organization_short_description
        Company_Founders['founder_primary_affiliation_organization_description'] = founder_primary_affiliation_organization_description
        Company_Founders['founder_primary_affiliation_organization_profile_image_url'] = founder_primary_affiliation_organization_profile_image_url
        Company_Founders['founder_primary_affiliation_organization_primary_role'] = founder_primary_affiliation_organization_primary_role
        Company_Founders['founder_primary_affiliation_organization_role_company'] = founder_primary_affiliation_organization_role_company
        Company_Founders['founder_primary_affiliation_organization_role_investor'] = founder_primary_affiliation_organization_role_investor
        Company_Founders['founder_primary_affiliation_organization_role_group'] = founder_primary_affiliation_organization_role_group
        Company_Founders['founder_primary_affiliation_organization_role_school'] = founder_primary_affiliation_organization_role_school
        Company_Founders['founder_primary_affiliation_organization_investor_type'] = founder_primary_affiliation_organization_investor_type
        Company_Founders['founder_primary_affiliation_organization_founded_on'] = founder_primary_affiliation_organization_founded_on
        Company_Founders['founder_primary_affiliation_organization_founded_on_trust_code'] = founder_primary_affiliation_organization_founded_on_trust_code
        Company_Founders['founder_primary_affiliation_organization_is_closed'] = founder_primary_affiliation_organization_is_closed
        Company_Founders['founder_primary_affiliation_organization_closed_on'] = founder_primary_affiliation_organization_closed_on
        Company_Founders['founder_primary_affiliation_organization_closed_on_trust_code'] = founder_primary_affiliation_organization_closed_on_trust_code
        Company_Founders['founder_primary_affiliation_organization_num_employees_min'] = founder_primary_affiliation_organization_num_employees_min
        Company_Founders['founder_primary_affiliation_organization_num_employees_max'] = founder_primary_affiliation_organization_num_employees_max
        Company_Founders['founder_primary_affiliation_organization_stock_exchange'] = founder_primary_affiliation_organization_stock_exchange
        Company_Founders['founder_primary_affiliation_organization_stock_symbol'] = founder_primary_affiliation_organization_stock_symbol
        Company_Founders['founder_primary_affiliation_organization_total_funding_usd'] = founder_primary_affiliation_organization_total_funding_usd
        Company_Founders['founder_primary_affiliation_organization_number_of_investments'] = founder_primary_affiliation_organization_number_of_investments
        Company_Founders['founder_primary_affiliation_organization_homepage_url'] = founder_primary_affiliation_organization_homepage_url
        Company_Founders['founder_primary_affiliation_organization_contact_email'] = founder_primary_affiliation_organization_contact_email
        Company_Founders['founder_primary_affiliation_organization_phone_number'] = founder_primary_affiliation_organization_phone_number
        Company_Founders['founder_primary_affiliation_organization_rank'] = founder_primary_affiliation_organization_rank
        Company_Founders['founder_primary_affiliation_organization_created_at'] = founder_primary_affiliation_organization_created_at
        Company_Founders['founder_primary_affiliation_organization_updated_at'] = founder_primary_affiliation_organization_updated_at
        Company_Founders['founder_primary_image_type'] = founder_primary_image_type
        Company_Founders['founder_primary_image_uuid'] = founder_primary_image_uuid
        Company_Founders['founder_primary_image_asset_path'] = founder_primary_image_asset_path
        Company_Founders['founder_primary_image_asset_url'] = founder_primary_image_asset_url
        Company_Founders['founder_primary_image_content_type'] = founder_primary_image_content_type
        Company_Founders['founder_primary_image_height'] = founder_primary_image_height
        Company_Founders['founder_primary_image_width'] = founder_primary_image_width
        Company_Founders['founder_primary_image_filesize'] = founder_primary_image_filesize
        Company_Founders['founder_primary_image_created_at'] = founder_primary_image_created_at
        Company_Founders['founder_primary_image_updated_at'] = founder_primary_image_updated_at
        
        # Output data frame for CompanyFounders_Degrees
        Company_Founders_Degrees['company_uuid'] = company_uuid_founder_degree
        Company_Founders_Degrees['company_name'] = company_name_founder_degree
        Company_Founders_Degrees['founder_uuid'] = founder_uuid_founder_degree
        Company_Founders_Degrees['founder_first_name'] = founder_first_name_founder_degree
        Company_Founders_Degrees['founder_last_name'] = founder_last_name_founder_degree
        Company_Founders_Degrees['founder_degree_type'] = founder_degree_type
        Company_Founders_Degrees['founder_degree_uuid'] = founder_degree_uuid
        Company_Founders_Degrees['founder_degree_started_on'] = founder_degree_started_on
        Company_Founders_Degrees['founder_degree_started_on_trust_code'] = founder_degree_started_on_trust_code
        Company_Founders_Degrees['founder_degree_completed_on'] = founder_degree_completed_on
        Company_Founders_Degrees['founder_degree_completed_on_trust_code'] = founder_degree_completed_on_trust_code
        Company_Founders_Degrees['founder_degree_type_name'] = founder_degree_type_name
        Company_Founders_Degrees['founder_degree_subject'] = founder_degree_subject
        Company_Founders_Degrees['founder_degree_created_at'] = founder_degree_created_at
        Company_Founders_Degrees['founder_degree_updated_at'] = founder_degree_updated_at
        Company_Founders_Degrees['founder_degree_school_type'] = founder_degree_school_type
        Company_Founders_Degrees['founder_degree_school_uuid'] = founder_degree_school_uuid
        Company_Founders_Degrees['founder_degree_school_permalink'] = founder_degree_school_permalink
        Company_Founders_Degrees['founder_degree_school_permalink_aliases'] = founder_degree_school_permalink_aliases
        Company_Founders_Degrees['founder_degree_school_api_path'] = founder_degree_school_api_path
        Company_Founders_Degrees['founder_degree_school_web_path'] = founder_degree_school_web_path
        Company_Founders_Degrees['founder_degree_school_api_url'] = founder_degree_school_api_url
        Company_Founders_Degrees['founder_degree_school_name'] = founder_degree_school_name
        Company_Founders_Degrees['founder_degree_school_also_known_as'] = founder_degree_school_also_known_as
        Company_Founders_Degrees['founder_degree_school_short_description'] = founder_degree_school_short_description
        Company_Founders_Degrees['founder_degree_school_description'] = founder_degree_school_description
        Company_Founders_Degrees['founder_degree_school_profile_image_url'] = founder_degree_school_profile_image_url
        Company_Founders_Degrees['founder_degree_school_primary_role'] = founder_degree_school_primary_role
        Company_Founders_Degrees['founder_degree_school_role_company'] = founder_degree_school_role_company
        Company_Founders_Degrees['founder_degree_school_role_investor'] = founder_degree_school_role_investor
        Company_Founders_Degrees['founder_degree_school_role_group'] = founder_degree_school_role_group
        Company_Founders_Degrees['founder_degree_school_role_school'] = founder_degree_school_role_school
        Company_Founders_Degrees['founder_degree_school_investor_type'] = founder_degree_school_investor_type
        Company_Founders_Degrees['founder_degree_school_founded_on'] = founder_degree_school_founded_on
        Company_Founders_Degrees['founder_degree_school_founded_on_trust_code'] = founder_degree_school_founded_on_trust_code
        Company_Founders_Degrees['founder_degree_school_is_closed'] = founder_degree_school_is_closed
        Company_Founders_Degrees['founder_degree_school_closed_on'] = founder_degree_school_closed_on
        Company_Founders_Degrees['founder_degree_school_closed_on_trust_code'] = founder_degree_school_closed_on_trust_code
        Company_Founders_Degrees['founder_degree_school_num_employees_min'] = founder_degree_school_num_employees_min
        Company_Founders_Degrees['founder_degree_school_num_employees_max'] = founder_degree_school_num_employees_max
        Company_Founders_Degrees['founder_degree_school_stock_exchange'] = founder_degree_school_stock_exchange
        Company_Founders_Degrees['founder_degree_school_stock_symbol'] = founder_degree_school_stock_symbol
        Company_Founders_Degrees['founder_degree_school_total_funding_usd'] = founder_degree_school_total_funding_usd
        Company_Founders_Degrees['founder_degree_school_number_of_investments'] = founder_degree_school_number_of_investments
        Company_Founders_Degrees['founder_degree_school_homepage_url'] = founder_degree_school_homepage_url
        Company_Founders_Degrees['founder_degree_school_contact_email'] = founder_degree_school_contact_email
        Company_Founders_Degrees['founder_degree_school_phone_number'] = founder_degree_school_phone_number
        Company_Founders_Degrees['founder_degree_school_rank'] = founder_degree_school_rank
        Company_Founders_Degrees['founder_degree_school_created_at'] = founder_degree_school_created_at
        Company_Founders_Degrees['founder_degree_school_updated_at'] = founder_degree_school_updated_at
        
        # Output data frame for CompanyFounders_Jobs
        Company_Founders_Jobs['company_uuid'] = company_uuid_founder_job
        Company_Founders_Jobs['company_name'] = company_name_founder_job
        Company_Founders_Jobs['founder_uuid'] = founder_uuid_founder_job
        Company_Founders_Jobs['founder_first_name'] = founder_first_name_founder_job
        Company_Founders_Jobs['founder_last_name'] = founder_last_name_founder_job
        Company_Founders_Jobs['founder_job_type'] = founder_job_type
        Company_Founders_Jobs['founder_job_uuid'] = founder_job_uuid
        Company_Founders_Jobs['founder_job_title'] = founder_job_title
        Company_Founders_Jobs['founder_job_started_on'] = founder_job_started_on
        Company_Founders_Jobs['founder_job_started_on_trust_code'] = founder_job_started_on_trust_code
        Company_Founders_Jobs['founder_job_ended_on'] = founder_job_ended_on
        Company_Founders_Jobs['founder_job_ended_on_trust_code'] = founder_job_ended_on_trust_code
        Company_Founders_Jobs['founder_job_is_current'] = founder_job_is_current
        Company_Founders_Jobs['founder_job_job_type'] = founder_job_job_type
        Company_Founders_Jobs['founder_job_created_at'] = founder_job_created_at
        Company_Founders_Jobs['founder_job_updated_at'] = founder_job_updated_at
        Company_Founders_Jobs['founder_job_organization_type'] = founder_job_organization_type
        Company_Founders_Jobs['founder_job_organization_uuid'] = founder_job_organization_uuid
        Company_Founders_Jobs['founder_job_organization_permalink'] = founder_job_organization_permalink
        Company_Founders_Jobs['founder_job_organization_permalink_aliases'] = founder_job_organization_permalink_aliases
        Company_Founders_Jobs['founder_job_organization_api_path'] = founder_job_organization_api_path
        Company_Founders_Jobs['founder_job_organization_web_path'] = founder_job_organization_web_path
        Company_Founders_Jobs['founder_job_organization_api_url'] = founder_job_organization_api_url
        Company_Founders_Jobs['founder_job_organization_name'] = founder_job_organization_name
        Company_Founders_Jobs['founder_job_organization_also_known_as'] = founder_job_organization_also_known_as
        Company_Founders_Jobs['founder_job_organization_short_description'] = founder_job_organization_short_description
        Company_Founders_Jobs['founder_job_organization_description'] = founder_job_organization_description
        Company_Founders_Jobs['founder_job_organization_profile_image_url'] = founder_job_organization_profile_image_url
        Company_Founders_Jobs['founder_job_organization_primary_role'] = founder_job_organization_primary_role
        Company_Founders_Jobs['founder_job_organization_role_company'] = founder_job_organization_role_company
        Company_Founders_Jobs['founder_job_organization_role_investor'] = founder_job_organization_role_investor
        Company_Founders_Jobs['founder_job_organization_role_group'] = founder_job_organization_role_group
        Company_Founders_Jobs['founder_job_organization_role_school'] = founder_job_organization_role_school
        Company_Founders_Jobs['founder_job_organization_investor_type'] = founder_job_organization_investor_type
        Company_Founders_Jobs['founder_job_organization_founded_on'] = founder_job_organization_founded_on
        Company_Founders_Jobs['founder_job_organization_founded_on_trust_code'] = founder_job_organization_founded_on_trust_code
        Company_Founders_Jobs['founder_job_organization_is_closed'] = founder_job_organization_is_closed
        Company_Founders_Jobs['founder_job_organization_closed_on'] = founder_job_organization_closed_on
        Company_Founders_Jobs['founder_job_organization_closed_on_trust_code'] = founder_job_organization_closed_on_trust_code
        Company_Founders_Jobs['founder_job_organization_num_employees_min'] = founder_job_organization_num_employees_min
        Company_Founders_Jobs['founder_job_organization_num_employees_max'] = founder_job_organization_num_employees_max
        Company_Founders_Jobs['founder_job_organization_stock_exchange'] = founder_job_organization_stock_exchange
        Company_Founders_Jobs['founder_job_organization_stock_symbol'] = founder_job_organization_stock_symbol
        Company_Founders_Jobs['founder_job_organization_total_funding_usd'] = founder_job_organization_total_funding_usd
        Company_Founders_Jobs['founder_job_organization_number_of_investments'] = founder_job_organization_number_of_investments
        Company_Founders_Jobs['founder_job_organization_homepage_url'] = founder_job_organization_homepage_url
        Company_Founders_Jobs['founder_job_organization_contact_email'] = founder_job_organization_contact_email
        Company_Founders_Jobs['founder_job_organization_phone_number'] = founder_job_organization_phone_number
        Company_Founders_Jobs['founder_job_organization_rank'] = founder_job_organization_rank
        Company_Founders_Jobs['founder_job_organization_created_at'] = founder_job_organization_created_at
        Company_Founders_Jobs['founder_job_organization_updated_at'] = founder_job_organization_updated_at
        
        # Output data frame for CompanyFounders_FoundedCompanies
        Company_Founders_FoundedCompanies['company_uuid'] = company_uuid_founder_founded_company
        Company_Founders_FoundedCompanies['company_name'] = company_name_founder_founded_company
        Company_Founders_FoundedCompanies['founder_uuid'] = founder_uuid_founder_founded_company
        Company_Founders_FoundedCompanies['founder_first_name'] = founder_first_name_founder_founded_company
        Company_Founders_FoundedCompanies['founder_last_name'] = founder_last_name_founder_founded_company
        Company_Founders_FoundedCompanies['founder_founded_company_type'] = founder_founded_company_type
        Company_Founders_FoundedCompanies['founder_founded_company_uuid'] = founder_founded_company_uuid
        Company_Founders_FoundedCompanies['founder_founded_company_permalink'] = founder_founded_company_permalink
        Company_Founders_FoundedCompanies['founder_founded_company_permalink_aliases'] = founder_founded_company_permalink_aliases
        Company_Founders_FoundedCompanies['founder_founded_company_api_path'] = founder_founded_company_api_path
        Company_Founders_FoundedCompanies['founder_founded_company_web_path'] = founder_founded_company_web_path
        Company_Founders_FoundedCompanies['founder_founded_company_api_url'] = founder_founded_company_api_url
        Company_Founders_FoundedCompanies['founder_founded_company_name'] = founder_founded_company_name
        Company_Founders_FoundedCompanies['founder_founded_company_also_known_as'] = founder_founded_company_also_known_as
        Company_Founders_FoundedCompanies['founder_founded_company_short_description'] = founder_founded_company_short_description
        Company_Founders_FoundedCompanies['founder_founded_company_description'] = founder_founded_company_description
        Company_Founders_FoundedCompanies['founder_founded_company_profile_image_url'] = founder_founded_company_profile_image_url
        Company_Founders_FoundedCompanies['founder_founded_company_primary_role'] = founder_founded_company_primary_role
        Company_Founders_FoundedCompanies['founder_founded_company_role_company'] = founder_founded_company_role_company
        Company_Founders_FoundedCompanies['founder_founded_company_role_investor'] = founder_founded_company_role_investor
        Company_Founders_FoundedCompanies['founder_founded_company_role_group'] = founder_founded_company_role_group
        Company_Founders_FoundedCompanies['founder_founded_company_role_school'] = founder_founded_company_role_school
        Company_Founders_FoundedCompanies['founder_founded_company_investor_type'] = founder_founded_company_investor_type
        Company_Founders_FoundedCompanies['founder_founded_company_founded_on'] = founder_founded_company_founded_on
        Company_Founders_FoundedCompanies['founder_founded_company_founded_on_trust_code'] = founder_founded_company_founded_on_trust_code
        Company_Founders_FoundedCompanies['founder_founded_company_is_closed'] = founder_founded_company_is_closed
        Company_Founders_FoundedCompanies['founder_founded_company_closed_on'] = founder_founded_company_closed_on
        Company_Founders_FoundedCompanies['founder_founded_company_closed_on_trust_code'] = founder_founded_company_closed_on_trust_code
        Company_Founders_FoundedCompanies['founder_founded_company_num_employees_min'] = founder_founded_company_num_employees_min
        Company_Founders_FoundedCompanies['founder_founded_company_num_employees_max'] = founder_founded_company_num_employees_max
        Company_Founders_FoundedCompanies['founder_founded_company_stock_exchange'] = founder_founded_company_stock_exchange
        Company_Founders_FoundedCompanies['founder_founded_company_stock_symbol'] = founder_founded_company_stock_symbol
        Company_Founders_FoundedCompanies['founder_founded_company_total_funding_usd'] = founder_founded_company_total_funding_usd
        Company_Founders_FoundedCompanies['founder_founded_company_number_of_investments'] = founder_founded_company_number_of_investments
        Company_Founders_FoundedCompanies['founder_founded_company_homepage_url'] = founder_founded_company_homepage_url
        Company_Founders_FoundedCompanies['founder_founded_company_contact_email'] = founder_founded_company_contact_email
        Company_Founders_FoundedCompanies['founder_founded_company_phone_number'] = founder_founded_company_phone_number
        Company_Founders_FoundedCompanies['founder_founded_company_rank'] = founder_founded_company_rank
        Company_Founders_FoundedCompanies['founder_founded_company_created_at'] = founder_founded_company_created_at
        Company_Founders_FoundedCompanies['founder_founded_company_updated_at'] = founder_founded_company_updated_at   
        
        # Output data frame for CompanyFounders_Websites
        Company_Founders_Websites['company_uuid'] = company_uuid_founder_website
        Company_Founders_Websites['company_name'] = company_name_founder_website
        Company_Founders_Websites['founder_uuid'] = founder_uuid_founder_website
        Company_Founders_Websites['founder_first_name'] =  founder_first_name_founder_website
        Company_Founders_Websites['founder_last_name'] = founder_last_name_founder_website
        Company_Founders_Websites['founder_website_type'] = founder_website_type
        Company_Founders_Websites['founder_website_uuid'] = founder_website_uuid
        Company_Founders_Websites['founder_website_website_type'] = founder_website_website_type
        Company_Founders_Websites['founder_website_website_name'] = founder_website_website_name
        Company_Founders_Websites['founder_website_url'] = founder_website_url
        Company_Founders_Websites['founder_website_created_at'] = founder_website_created_at
        Company_Founders_Websites['founder_website_updated_at'] = founder_website_updated_at
        
        Company_Founders_AdvisoryRoles['company_uuid'] = company_uuid_founder_advisory_role
        Company_Founders_AdvisoryRoles['company_name'] = company_name_founder_advisory_role
        Company_Founders_AdvisoryRoles['founder_uuid'] = founder_uuid_founder_advisory_role
        Company_Founders_AdvisoryRoles['founder_first_name'] = founder_first_name_founder_advisory_role
        Company_Founders_AdvisoryRoles['founder_last_name'] = founder_last_name_founder_advisory_role
        Company_Founders_AdvisoryRoles['founder_advisory_role_type'] = founder_advisory_role_type
        Company_Founders_AdvisoryRoles['founder_advisory_role_uuid'] = founder_advisory_role_uuid
        Company_Founders_AdvisoryRoles['founder_advisory_role_title'] = founder_advisory_role_title
        Company_Founders_AdvisoryRoles['founder_advisory_role_started_on'] = founder_advisory_role_started_on
        Company_Founders_AdvisoryRoles['founder_advisory_role_started_on_trust_code'] = founder_advisory_role_started_on_trust_code
        Company_Founders_AdvisoryRoles['founder_advisory_role_ended_on'] = founder_advisory_role_ended_on
        Company_Founders_AdvisoryRoles['founder_advisory_role_ended_on_trust_code'] = founder_advisory_role_ended_on_trust_code
        Company_Founders_AdvisoryRoles['founder_advisory_role_is_current'] = founder_advisory_role_is_current
        Company_Founders_AdvisoryRoles['founder_advisory_role_job_type'] = founder_advisory_role_job_type
        Company_Founders_AdvisoryRoles['founder_advisory_role_created_at'] = founder_advisory_role_created_at
        Company_Founders_AdvisoryRoles['founder_advisory_role_updated_at'] = founder_advisory_role_updated_at
        Company_Founders_AdvisoryRoles['founder_advisory_role_organization_permalink'] = founder_advisory_role_organization_permalink
        Company_Founders_AdvisoryRoles['founder_advisory_role_organization_permalink_aliases'] = founder_advisory_role_organization_permalink_aliases
        Company_Founders_AdvisoryRoles['founder_advisory_role_organization_api_path'] = founder_advisory_role_organization_api_path
        Company_Founders_AdvisoryRoles['founder_advisory_role_organization_web_path'] = founder_advisory_role_organization_web_path
        Company_Founders_AdvisoryRoles['founder_advisory_role_organization_api_url'] = founder_advisory_role_organization_api_url
        Company_Founders_AdvisoryRoles['founder_advisory_role_organization_name'] = founder_advisory_role_organization_name
        Company_Founders_AdvisoryRoles['founder_advisory_role_organization_also_known_as'] = founder_advisory_role_organization_also_known_as
        Company_Founders_AdvisoryRoles['founder_advisory_role_organization_short_description'] = founder_advisory_role_organization_short_description
        Company_Founders_AdvisoryRoles['founder_advisory_role_organization_description'] = founder_advisory_role_organization_description
        Company_Founders_AdvisoryRoles['founder_advisory_role_organization_profile_image_url'] = founder_advisory_role_organization_profile_image_url
        Company_Founders_AdvisoryRoles['founder_advisory_role_organization_primary_role'] = founder_advisory_role_organization_primary_role
        Company_Founders_AdvisoryRoles['founder_advisory_role_organization_role_company'] = founder_advisory_role_organization_role_company
        Company_Founders_AdvisoryRoles['founder_advisory_role_organization_role_investor'] = founder_advisory_role_organization_role_investor
        Company_Founders_AdvisoryRoles['founder_advisory_role_organization_role_group'] = founder_advisory_role_organization_role_group
        Company_Founders_AdvisoryRoles['founder_advisory_role_organization_role_school'] = founder_advisory_role_organization_role_school
        Company_Founders_AdvisoryRoles['founder_advisory_role_organization_investor_type'] = founder_advisory_role_organization_investor_type
        Company_Founders_AdvisoryRoles['founder_advisory_role_organization_founded_on'] = founder_advisory_role_organization_founded_on
        Company_Founders_AdvisoryRoles['founder_advisory_role_organization_founded_on_trust_code'] = founder_advisory_role_organization_founded_on_trust_code
        Company_Founders_AdvisoryRoles['founder_advisory_role_organization_is_closed'] = founder_advisory_role_organization_is_closed
        Company_Founders_AdvisoryRoles['founder_advisory_role_organization_closed_on'] = founder_advisory_role_organization_closed_on
        Company_Founders_AdvisoryRoles['founder_advisory_role_organization_closed_on_trust_code'] = founder_advisory_role_organization_closed_on_trust_code
        Company_Founders_AdvisoryRoles['founder_advisory_role_organization_num_employees_min'] = founder_advisory_role_organization_num_employees_min
        Company_Founders_AdvisoryRoles['founder_advisory_role_organization_num_employees_max'] = founder_advisory_role_organization_num_employees_max
        Company_Founders_AdvisoryRoles['founder_advisory_role_organization_stock_exchange'] = founder_advisory_role_organization_stock_exchange
        Company_Founders_AdvisoryRoles['founder_advisory_role_organization_stock_symbol'] = founder_advisory_role_organization_stock_symbol
        Company_Founders_AdvisoryRoles['founder_advisory_role_organization_total_funding_usd'] = founder_advisory_role_organization_total_funding_usd
        Company_Founders_AdvisoryRoles['founder_advisory_role_organization_number_of_investments'] = founder_advisory_role_organization_number_of_investments
        Company_Founders_AdvisoryRoles['founder_advisory_role_organization_homepage_url'] = founder_advisory_role_organization_homepage_url
        Company_Founders_AdvisoryRoles['founder_advisory_role_organization_contact_email'] = founder_advisory_role_organization_contact_email
        Company_Founders_AdvisoryRoles['founder_advisory_role_organization_phone_number'] = founder_advisory_role_organization_phone_number
        Company_Founders_AdvisoryRoles['founder_advisory_role_organization_rank'] = founder_advisory_role_organization_rank
        Company_Founders_AdvisoryRoles['founder_advisory_role_organization_created_at'] = founder_advisory_role_organization_created_at
        Company_Founders_AdvisoryRoles['founder_advisory_role_organization_updated_at'] = founder_advisory_role_organization_updated_at
        
        Company_Founders_Investments['company_uuid'] = company_uuid_founder_investments
        Company_Founders_Investments['company_name'] = company_name_founder_investments
        Company_Founders_Investments['founder_uuid'] = founder_uuid_founder_investments
        Company_Founders_Investments['founder_first_name'] = founder_first_name_investments
        Company_Founders_Investments['founder_last_name'] = founder_last_name_founder_investments
        Company_Founders_Investments['founder_investment_type'] = founder_investment_type
        Company_Founders_Investments['founder_investment_uuid'] = founder_investment_uuid
        Company_Founders_Investments['founder_investment_money_invested'] = founder_investment_money_invested
        Company_Founders_Investments['founder_investment_money_invested_currency_code'] = founder_investment_money_invested_currency_code
        Company_Founders_Investments['founder_investment_money_invested_usd'] = founder_investment_money_invested_usd
        Company_Founders_Investments['founder_investment_is_lead_investor'] = founder_investment_is_lead_investor
        Company_Founders_Investments['founder_investment_announced_on'] = founder_investment_announced_on
        Company_Founders_Investments['founder_investment_announced_on_trust_code'] = founder_investment_announced_on_trust_code
        Company_Founders_Investments['founder_investment_created_at'] = founder_investment_created_at
        Company_Founders_Investments['founder_investment_updated_at'] = founder_investment_updated_at
        Company_Founders_Investments['founder_investment_funding_round_type'] = founder_investment_funding_round_type
        Company_Founders_Investments['founder_investment_funding_round_uuid'] = founder_investment_funding_round_uuid
        Company_Founders_Investments['founder_investment_funding_round_permalink'] = founder_investment_funding_round_permalink
        Company_Founders_Investments['founder_investment_funding_round_api_path'] = founder_investment_funding_round_api_path
        Company_Founders_Investments['founder_investment_funding_round_web_path'] = founder_investment_funding_round_web_path
        Company_Founders_Investments['founder_investment_funding_round_api_url'] = founder_investment_funding_round_api_url
        Company_Founders_Investments['founder_investment_funding_round_funding_type'] = founder_investment_funding_round_funding_type
        Company_Founders_Investments['founder_investment_funding_round_series'] = founder_investment_funding_round_series
        Company_Founders_Investments['founder_investment_funding_round_series_qualifier'] = founder_investment_funding_round_series_qualifier
        Company_Founders_Investments['founder_investment_funding_round_announced_on'] = founder_investment_funding_round_announced_on
        Company_Founders_Investments['founder_investment_funding_round_announced_on_trust_code'] = founder_investment_funding_round_announced_on_trust_code
        Company_Founders_Investments['founder_investment_funding_round_closed_on'] = founder_investment_funding_round_closed_on
        Company_Founders_Investments['founder_investment_funding_round_closed_on_trust_code'] = founder_investment_funding_round_closed_on_trust_code
        Company_Founders_Investments['founder_investment_funding_money_raised'] = founder_investment_funding_money_raised
        Company_Founders_Investments['founder_investment_funding_round_money_raised_currency_code'] = founder_investment_funding_round_money_raised_currency_code
        Company_Founders_Investments['founder_investment_funding_round_money_raised_usd'] = founder_investment_funding_round_money_raised_usd
        Company_Founders_Investments['founder_investment_funding_round_target_money_raised'] = founder_investment_funding_round_target_money_raised
        Company_Founders_Investments['founder_investment_funding_round_target_money_raised_currency_code'] = founder_investment_funding_round_target_money_raised_currency_code
        Company_Founders_Investments['founder_investment_funding_round_target_money_raised_usd'] = founder_investment_funding_round_target_money_raised_usd
        Company_Founders_Investments['founder_investment_funding_round_pre_money_valuation'] = founder_investment_funding_round_pre_money_valuation
        Company_Founders_Investments['founder_investment_funding_round_pre_money_valuation_currency_code'] = founder_investment_funding_round_pre_money_valuation_currency_code
        Company_Founders_Investments['founder_investment_funding_round_pre_money_valuation_usd'] = founder_investment_funding_round_pre_money_valuation_usd
        Company_Founders_Investments['founder_investment_funding_round_rank'] = founder_investment_funding_round_rank
        Company_Founders_Investments['founder_investment_funding_round_created_at'] = founder_investment_funding_round_created_at
        Company_Founders_Investments['founder_investment_funding_round_updated_at'] = founder_investment_funding_round_updated_at
        Company_Founders_Investments['founder_investment_funding_round_funded_organization_type'] = founder_investment_funding_round_funded_organization_type
        Company_Founders_Investments['founder_investment_funding_round_funded_organization_uuid'] = founder_investment_funding_round_funded_organization_uuid
        Company_Founders_Investments['founder_investment_funding_round_funded_organization_permalink'] = founder_investment_funding_round_funded_organization_permalink
        Company_Founders_Investments['founder_investment_funding_round_funded_organization_permalink_aliases'] = founder_investment_funding_round_funded_organization_permalink_aliases
        Company_Founders_Investments['founder_investment_funding_round_funded_organization_api_path'] = founder_investment_funding_round_funded_organization_api_path
        Company_Founders_Investments['founder_investment_funding_round_funded_organization_web_path'] = founder_investment_funding_round_funded_organization_web_path
        Company_Founders_Investments['founder_investment_funding_round_funded_organization_api_url'] = founder_investment_funding_round_funded_organization_api_url
        Company_Founders_Investments['founder_investment_funding_round_funded_organization_name'] = founder_investment_funding_round_funded_organization_name
        Company_Founders_Investments['founder_investment_funding_round_funded_organization_also_known_as'] = founder_investment_funding_round_funded_organization_also_known_as
        Company_Founders_Investments['founder_investment_funding_round_funded_organization_short_description'] = founder_investment_funding_round_funded_organization_short_description
        Company_Founders_Investments['founder_investment_funding_round_funded_organization_description'] = founder_investment_funding_round_funded_organization_description
        Company_Founders_Investments['founder_investment_funding_round_funded_organization_profile_image_url'] = founder_investment_funding_round_funded_organization_profile_image_url
        Company_Founders_Investments['founder_investment_funding_round_funded_organization_primary_role'] = founder_investment_funding_round_funded_organization_primary_role
        Company_Founders_Investments['founder_investment_funding_round_funded_organization_role_company'] = founder_investment_funding_round_funded_organization_role_company
        Company_Founders_Investments['founder_investment_funding_round_funded_organization_role_investor'] = founder_investment_funding_round_funded_organization_role_investor
        Company_Founders_Investments['founder_investment_funding_round_funded_organization_role_group'] = founder_investment_funding_round_funded_organization_role_group
        Company_Founders_Investments['founder_investment_funding_round_funded_organization_role_school'] = founder_investment_funding_round_funded_organization_role_school
        Company_Founders_Investments['founder_investment_funding_round_funded_organization_investor_type'] = founder_investment_funding_round_funded_organization_investor_type
        Company_Founders_Investments['founder_investment_funding_round_funded_organization_founded_on'] = founder_investment_funding_round_funded_organization_founded_on
        Company_Founders_Investments['founder_investment_funding_round_funded_organization_founded_on_trust_code'] = founder_investment_funding_round_funded_organization_founded_on_trust_code
        Company_Founders_Investments['founder_investment_funding_round_funded_organization_is_closed'] = founder_investment_funding_round_funded_organization_is_closed
        Company_Founders_Investments['founder_investment_funding_round_funded_organization_closed_on'] = founder_investment_funding_round_funded_organization_closed_on
        Company_Founders_Investments['founder_investment_funding_round_funded_organization_closed_on_trust_code'] = founder_investment_funding_round_funded_organization_closed_on_trust_code
        Company_Founders_Investments['founder_investment_funding_round_funded_organization_num_employees_min'] = founder_investment_funding_round_funded_organization_num_employees_min
        Company_Founders_Investments['founder_investment_funding_round_funded_organization_num_employees_max'] = founder_investment_funding_round_funded_organization_num_employees_max
        Company_Founders_Investments['founder_investment_funding_round_funded_organization_stock_exchange'] = founder_investment_funding_round_funded_organization_stock_exchange
        Company_Founders_Investments['founder_investment_funding_round_funded_organization_stock_symbol'] = founder_investment_funding_round_funded_organization_stock_symbol
        Company_Founders_Investments['founder_investment_funding_round_funded_organization_total_funding_usd'] = founder_investment_funding_round_funded_organization_total_funding_usd
        Company_Founders_Investments['founder_investment_funding_round_funded_organization_number_of_investments'] = founder_investment_funding_round_funded_organization_number_of_investments
        Company_Founders_Investments['founder_investment_funding_round_funded_organization_homepage_url'] = founder_investment_funding_round_funded_organization_homepage_url
        Company_Founders_Investments['founder_investment_funding_round_funded_organization_contact_email'] = founder_investment_funding_round_funded_organization_contact_email
        Company_Founders_Investments['founder_investment_funding_round_funded_organization_phone_number'] = founder_investment_funding_round_funded_organization_phone_number
        Company_Founders_Investments['founder_investment_funding_round_funded_organization_rank'] = founder_investment_funding_round_funded_organization_rank
        Company_Founders_Investments['founder_investment_funding_round_funded_organization_created_at'] = founder_investment_funding_round_funded_organization_created_at
        Company_Founders_Investments['founder_investment_funding_round_funded_organization_updated_at'] = founder_investment_funding_round_funded_organization_updated_at
    
  
         
    
    
    
        # Output data frame for Company_BoardMembers
        Company_BoardMembers['company_uuid_board_details']=company_uuid_board_details
        Company_BoardMembers['company_name_board_details']=company_name_board_details
        Company_BoardMembers['board_uuid'] = board_details_uuid
        Company_BoardMembers['board_details_title'] = board_details_title
        Company_BoardMembers['board_details_started_on'] =board_details_started_on
        Company_BoardMembers['board_details_started_on_trust_code'] = board_details_started_on_trust_code
        Company_BoardMembers['board_details_ended_on'] = board_details_ended_on
        Company_BoardMembers['board_details_is_current'] = board_details_is_current
        Company_BoardMembers['board_details_job_type'] =board_details_job_type
        Company_BoardMembers['board_details_created_at'] =board_details_created_at
        Company_BoardMembers['board_details_updated_at'] = board_details_updated_at
        Company_BoardMembers['board_details_type']=board_details_type
        Company_BoardMembers['board_details_person_uuid']=board_details_person_uuid
        Company_BoardMembers['board_details_person_permalink']=board_details_person_permalink
        Company_BoardMembers['board_details_person_permalink_aliases']=board_details_person_permalink_aliases
        Company_BoardMembers['board_details_person_api_path']=board_details_person_api_path
        Company_BoardMembers['board_details_person_web_path']=board_details_person_web_path
        Company_BoardMembers['board_details_person_api_url']=board_details_person_api_url
        Company_BoardMembers['board_details_person_first_name']=board_details_person_first_name
        Company_BoardMembers['board_details_person_last_name']=board_details_person_last_name
        Company_BoardMembers['board_details_person_gender']=board_details_person_gender
        Company_BoardMembers['board_details_person_also_known_as']=board_details_person_also_known_as
        Company_BoardMembers['board_details_person_bio']=board_details_person_bio
        Company_BoardMembers['board_details_person_profile_image_url']=board_details_person_profile_image_url
        Company_BoardMembers['board_details_person_role_investor']=board_details_person_role_investor
        Company_BoardMembers['board_details_person_born_on']=board_details_person_born_on
        Company_BoardMembers['board_details_person_born_on_trust_code']=board_details_person_born_on_trust_code
        Company_BoardMembers['board_details_person_died_on']=board_details_person_died_on
        Company_BoardMembers['board_details_person_died_on_trust_code']=board_details_person_died_on_trust_code
        Company_BoardMembers['board_details_person_rank']=board_details_person_rank
        Company_BoardMembers['board_details_person_created_at']=board_details_person_created_at
        Company_BoardMembers['board_details_person_updated_at']=board_details_person_updated_at
        Company_BoardMembers['BoardMembers_primary_location_type'] = BoardMembers_primary_location_type
        Company_BoardMembers['BoardMembers_primary_location_uuid'] = BoardMembers_primary_location_uuid
        Company_BoardMembers['BoardMembers_primary_location_uuid'] = BoardMembers_primary_location_uuid
        Company_BoardMembers['BoardMembers_primary_location_location_type'] = BoardMembers_primary_location_location_type
        Company_BoardMembers['BoardMembers_primary_location_parent_location_uuid'] = BoardMembers_primary_location_parent_location_uuid
        Company_BoardMembers['BoardMembers_primary_location_city'] = BoardMembers_primary_location_city
        Company_BoardMembers['BoardMembers_primary_location_region'] = BoardMembers_primary_location_region
        Company_BoardMembers['BoardMembers_primary_location_region_code2'] = BoardMembers_primary_location_region_code2
        Company_BoardMembers['BoardMembers_primary_location_country'] = BoardMembers_primary_location_country
        Company_BoardMembers['BoardMembers_primary_location_country_code2'] = BoardMembers_primary_location_country_code2
        Company_BoardMembers['BoardMembers_primary_location_country_code3'] = BoardMembers_primary_location_country_code3
        Company_BoardMembers['BoardMembers_primary_location_continent'] = BoardMembers_primary_location_continent
        Company_BoardMembers['BoardMembers_primary_location_created_at'] = BoardMembers_primary_location_created_at
        Company_BoardMembers['BoardMembers_primary_location_updated_at'] = BoardMembers_primary_location_updated_at
        Company_BoardMembers['BoardMembers_primary_affiliation_type'] = BoardMembers_primary_affiliation_type
        Company_BoardMembers['BoardMembers_primary_affiliation_uuid'] = BoardMembers_primary_affiliation_uuid
        Company_BoardMembers['BoardMembers_primary_affiliation_title'] = BoardMembers_primary_affiliation_title
        Company_BoardMembers['BoardMembers_primary_affiliation_started_on'] = BoardMembers_primary_affiliation_started_on
        Company_BoardMembers['BoardMembers_primary_affiliation_started_on_trust_code'] = BoardMembers_primary_affiliation_started_on_trust_code
        Company_BoardMembers['BoardMembers_primary_affiliation_ended_on'] = BoardMembers_primary_affiliation_ended_on
        Company_BoardMembers['BoardMembers_primary_affiliation_ended_on_trust_code'] = BoardMembers_primary_affiliation_ended_on_trust_code   
        Company_BoardMembers['BoardMembers_primary_affiliation_is_current'] = BoardMembers_primary_affiliation_is_current
        Company_BoardMembers['BoardMembers_primary_affiliation_job_type'] = BoardMembers_primary_affiliation_job_type
        Company_BoardMembers['BoardMembers_primary_affiliation_created_at'] = BoardMembers_primary_affiliation_created_at
        Company_BoardMembers['BoardMembers_primary_affiliation_updated_at'] = BoardMembers_primary_affiliation_updated_at
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_type'] = BoardMembers_primary_affiliation_organization_type
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_uuid'] = BoardMembers_primary_affiliation_organization_uuid
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_permalink'] = BoardMembers_primary_affiliation_organization_permalink
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_permalink_aliases'] = BoardMembers_primary_affiliation_organization_permalink_aliases
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_api_path'] = BoardMembers_primary_affiliation_organization_api_path
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_web_path'] = BoardMembers_primary_affiliation_organization_web_path
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_api_url'] = BoardMembers_primary_affiliation_organization_api_url
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_name'] = BoardMembers_primary_affiliation_organization_name
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_also_known_as'] = BoardMembers_primary_affiliation_organization_also_known_as
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_short_description'] = BoardMembers_primary_affiliation_organization_short_description
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_description'] = BoardMembers_primary_affiliation_organization_description
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_profile_image_url'] = BoardMembers_primary_affiliation_organization_profile_image_url
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_primary_role'] = BoardMembers_primary_affiliation_organization_primary_role
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_role_company'] = BoardMembers_primary_affiliation_organization_role_company
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_role_investor'] = BoardMembers_primary_affiliation_organization_role_investor
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_role_group'] = BoardMembers_primary_affiliation_organization_role_group
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_role_school'] = BoardMembers_primary_affiliation_organization_role_school
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_investor_type'] = BoardMembers_primary_affiliation_organization_investor_type
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_founded_on'] = BoardMembers_primary_affiliation_organization_founded_on
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_founded_on_trust_code'] = BoardMembers_primary_affiliation_organization_founded_on_trust_code
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_is_closed'] = BoardMembers_primary_affiliation_organization_is_closed
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_closed_on'] = BoardMembers_primary_affiliation_organization_closed_on
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_closed_on_trust_code'] = BoardMembers_primary_affiliation_organization_closed_on_trust_code
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_num_employees_min'] = BoardMembers_primary_affiliation_organization_num_employees_min
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_num_employees_max'] = BoardMembers_primary_affiliation_organization_num_employees_max
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_stock_exchange'] = BoardMembers_primary_affiliation_organization_stock_exchange
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_stock_symbol'] = BoardMembers_primary_affiliation_organization_stock_symbol
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_total_funding_usd'] = BoardMembers_primary_affiliation_organization_total_funding_usd
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_number_of_investments'] = BoardMembers_primary_affiliation_organization_number_of_investments
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_homepage_url'] = BoardMembers_primary_affiliation_organization_homepage_url
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_contact_email'] = BoardMembers_primary_affiliation_organization_contact_email
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_phone_number'] = BoardMembers_primary_affiliation_organization_phone_number
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_rank'] = BoardMembers_primary_affiliation_organization_rank
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_created_at'] = BoardMembers_primary_affiliation_organization_created_at
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_updated_at'] = BoardMembers_primary_affiliation_organization_updated_at
        Company_BoardMembers['BoardMembers_primary_image_type'] = BoardMembers_primary_image_type
        Company_BoardMembers['BoardMembers_primary_image_uuid'] = BoardMembers_primary_image_uuid
        Company_BoardMembers['BoardMembers_primary_image_asset_path'] = BoardMembers_primary_image_asset_path
        Company_BoardMembers['BoardMembers_primary_image_asset_url'] = BoardMembers_primary_image_asset_url
        Company_BoardMembers['BoardMembers_primary_image_content_type'] = BoardMembers_primary_image_content_type
        Company_BoardMembers['BoardMembers_primary_image_height'] = BoardMembers_primary_image_height
        Company_BoardMembers['BoardMembers_primary_image_width'] = BoardMembers_primary_image_width
        Company_BoardMembers['BoardMembers_primary_image_filesize'] = BoardMembers_primary_image_filesize
        Company_BoardMembers['BoardMembers_primary_image_created_at'] = BoardMembers_primary_image_created_at
        Company_BoardMembers['BoardMembers_primary_image_updated_at'] = BoardMembers_primary_image_updated_at
        Company_BoardMembers['BoardMembers_primary_location_type'] = BoardMembers_primary_location_type
        Company_BoardMembers['BoardMembers_primary_location_uuid'] = BoardMembers_primary_location_uuid
        Company_BoardMembers['BoardMembers_primary_location_uuid'] = BoardMembers_primary_location_uuid
        Company_BoardMembers['BoardMembers_primary_location_location_type'] = BoardMembers_primary_location_location_type
        Company_BoardMembers['BoardMembers_primary_location_parent_location_uuid'] = BoardMembers_primary_location_parent_location_uuid
        Company_BoardMembers['BoardMembers_primary_location_city'] = BoardMembers_primary_location_city
        Company_BoardMembers['BoardMembers_primary_location_region'] = BoardMembers_primary_location_region
        Company_BoardMembers['BoardMembers_primary_location_region_code2'] = BoardMembers_primary_location_region_code2
        Company_BoardMembers['BoardMembers_primary_location_country'] = BoardMembers_primary_location_country
        Company_BoardMembers['BoardMembers_primary_location_country_code2'] = BoardMembers_primary_location_country_code2
        Company_BoardMembers['BoardMembers_primary_location_country_code3'] = BoardMembers_primary_location_country_code3
        Company_BoardMembers['BoardMembers_primary_location_continent'] = BoardMembers_primary_location_continent
        Company_BoardMembers['BoardMembers_primary_location_created_at'] = BoardMembers_primary_location_created_at
        Company_BoardMembers['BoardMembers_primary_location_updated_at'] = BoardMembers_primary_location_updated_at
        Company_BoardMembers['BoardMembers_primary_affiliation_type'] = BoardMembers_primary_affiliation_type
        Company_BoardMembers['BoardMembers_primary_affiliation_uuid'] = BoardMembers_primary_affiliation_uuid
        Company_BoardMembers['BoardMembers_primary_affiliation_title'] = BoardMembers_primary_affiliation_title
        Company_BoardMembers['BoardMembers_primary_affiliation_started_on'] = BoardMembers_primary_affiliation_started_on
        Company_BoardMembers['BoardMembers_primary_affiliation_started_on_trust_code'] = BoardMembers_primary_affiliation_started_on_trust_code
        Company_BoardMembers['BoardMembers_primary_affiliation_ended_on'] = BoardMembers_primary_affiliation_ended_on
        Company_BoardMembers['BoardMembers_primary_affiliation_ended_on_trust_code'] = BoardMembers_primary_affiliation_ended_on_trust_code   
        Company_BoardMembers['BoardMembers_primary_affiliation_is_current'] = BoardMembers_primary_affiliation_is_current
        Company_BoardMembers['BoardMembers_primary_affiliation_job_type'] = BoardMembers_primary_affiliation_job_type
        Company_BoardMembers['BoardMembers_primary_affiliation_created_at'] = BoardMembers_primary_affiliation_created_at
        Company_BoardMembers['BoardMembers_primary_affiliation_updated_at'] = BoardMembers_primary_affiliation_updated_at
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_type'] = BoardMembers_primary_affiliation_organization_type
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_uuid'] = BoardMembers_primary_affiliation_organization_uuid
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_permalink'] = BoardMembers_primary_affiliation_organization_permalink
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_permalink_aliases'] = BoardMembers_primary_affiliation_organization_permalink_aliases
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_api_path'] = BoardMembers_primary_affiliation_organization_api_path
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_web_path'] = BoardMembers_primary_affiliation_organization_web_path
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_api_url'] = BoardMembers_primary_affiliation_organization_api_url
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_name'] = BoardMembers_primary_affiliation_organization_name
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_also_known_as'] = BoardMembers_primary_affiliation_organization_also_known_as
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_short_description'] = BoardMembers_primary_affiliation_organization_short_description
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_description'] = BoardMembers_primary_affiliation_organization_description
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_profile_image_url'] = BoardMembers_primary_affiliation_organization_profile_image_url
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_primary_role'] = BoardMembers_primary_affiliation_organization_primary_role
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_role_company'] = BoardMembers_primary_affiliation_organization_role_company
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_role_investor'] = BoardMembers_primary_affiliation_organization_role_investor
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_role_group'] = BoardMembers_primary_affiliation_organization_role_group
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_role_school'] = BoardMembers_primary_affiliation_organization_role_school
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_investor_type'] = BoardMembers_primary_affiliation_organization_investor_type
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_founded_on'] = BoardMembers_primary_affiliation_organization_founded_on
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_founded_on_trust_code'] = BoardMembers_primary_affiliation_organization_founded_on_trust_code
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_is_closed'] = BoardMembers_primary_affiliation_organization_is_closed
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_closed_on'] = BoardMembers_primary_affiliation_organization_closed_on
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_closed_on_trust_code'] = BoardMembers_primary_affiliation_organization_closed_on_trust_code
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_num_employees_min'] = BoardMembers_primary_affiliation_organization_num_employees_min
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_num_employees_max'] = BoardMembers_primary_affiliation_organization_num_employees_max
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_stock_exchange'] = BoardMembers_primary_affiliation_organization_stock_exchange
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_stock_symbol'] = BoardMembers_primary_affiliation_organization_stock_symbol
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_total_funding_usd'] = BoardMembers_primary_affiliation_organization_total_funding_usd
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_number_of_investments'] = BoardMembers_primary_affiliation_organization_number_of_investments
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_homepage_url'] = BoardMembers_primary_affiliation_organization_homepage_url
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_contact_email'] = BoardMembers_primary_affiliation_organization_contact_email
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_phone_number'] = BoardMembers_primary_affiliation_organization_phone_number
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_rank'] = BoardMembers_primary_affiliation_organization_rank
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_created_at'] = BoardMembers_primary_affiliation_organization_created_at
        Company_BoardMembers['BoardMembers_primary_affiliation_organization_updated_at'] = BoardMembers_primary_affiliation_organization_updated_at
        Company_BoardMembers['BoardMembers_primary_image_type'] = BoardMembers_primary_image_type
        Company_BoardMembers['BoardMembers_primary_image_uuid'] = BoardMembers_primary_image_uuid
        Company_BoardMembers['BoardMembers_primary_image_asset_path'] = BoardMembers_primary_image_asset_path
        Company_BoardMembers['BoardMembers_primary_image_asset_url'] = BoardMembers_primary_image_asset_url
        Company_BoardMembers['BoardMembers_primary_image_content_type'] = BoardMembers_primary_image_content_type
        Company_BoardMembers['BoardMembers_primary_image_height'] = BoardMembers_primary_image_height
        Company_BoardMembers['BoardMembers_primary_image_width'] = BoardMembers_primary_image_width
        Company_BoardMembers['BoardMembers_primary_image_filesize'] = BoardMembers_primary_image_filesize
        Company_BoardMembers['BoardMembers_primary_image_created_at'] = BoardMembers_primary_image_created_at
        Company_BoardMembers['BoardMembers_primary_image_updated_at'] = BoardMembers_primary_image_updated_at
        Company_BoardMembers_Degrees['company_uuid'] = company_uuid_BoardMembers_degree
        Company_BoardMembers_Degrees['company_name'] = company_name_BoardMembers_degree
        Company_BoardMembers_Degrees['BoardMembers_uuid'] = BoardMembers_uuid_BoardMembers_degree
        Company_BoardMembers_Degrees['BoardMembers_first_name'] = BoardMembers_first_name_BoardMembers_degree
        Company_BoardMembers_Degrees['BoardMembers_last_name'] = BoardMembers_last_name_BoardMembers_degree
        Company_BoardMembers_Degrees['BoardMembers_degree_type'] = BoardMembers_degree_type
        Company_BoardMembers_Degrees['BoardMembers_degree_uuid'] = BoardMembers_degree_uuid
        Company_BoardMembers_Degrees['BoardMembers_degree_started_on'] = BoardMembers_degree_started_on
        Company_BoardMembers_Degrees['BoardMembers_degree_started_on_trust_code'] = BoardMembers_degree_started_on_trust_code
        Company_BoardMembers_Degrees['BoardMembers_degree_completed_on'] = BoardMembers_degree_completed_on
        Company_BoardMembers_Degrees['BoardMembers_degree_completed_on_trust_code'] = BoardMembers_degree_completed_on_trust_code
        Company_BoardMembers_Degrees['BoardMembers_degree_type_name'] = BoardMembers_degree_type_name
        Company_BoardMembers_Degrees['BoardMembers_degree_subject'] = BoardMembers_degree_subject
        Company_BoardMembers_Degrees['BoardMembers_degree_created_at'] = BoardMembers_degree_created_at
        Company_BoardMembers_Degrees['BoardMembers_degree_updated_at'] = BoardMembers_degree_updated_at
        Company_BoardMembers_Degrees['BoardMembers_degree_school_type'] = BoardMembers_degree_school_type
        Company_BoardMembers_Degrees['BoardMembers_degree_school_uuid'] = BoardMembers_degree_school_uuid
        Company_BoardMembers_Degrees['BoardMembers_degree_school_permalink'] = BoardMembers_degree_school_permalink
        Company_BoardMembers_Degrees['BoardMembers_degree_school_permalink_aliases'] = BoardMembers_degree_school_permalink_aliases
        Company_BoardMembers_Degrees['BoardMembers_degree_school_api_path'] = BoardMembers_degree_school_api_path
        Company_BoardMembers_Degrees['BoardMembers_degree_school_web_path'] = BoardMembers_degree_school_web_path
        Company_BoardMembers_Degrees['BoardMembers_degree_school_api_url'] = BoardMembers_degree_school_api_url
        Company_BoardMembers_Degrees['BoardMembers_degree_school_name'] = BoardMembers_degree_school_name
        Company_BoardMembers_Degrees['BoardMembers_degree_school_also_known_as'] = BoardMembers_degree_school_also_known_as
        Company_BoardMembers_Degrees['BoardMembers_degree_school_short_description'] = BoardMembers_degree_school_short_description
        Company_BoardMembers_Degrees['BoardMembers_degree_school_description'] = BoardMembers_degree_school_description
        Company_BoardMembers_Degrees['BoardMembers_degree_school_profile_image_url'] = BoardMembers_degree_school_profile_image_url
        Company_BoardMembers_Degrees['BoardMembers_degree_school_primary_role'] = BoardMembers_degree_school_primary_role
        Company_BoardMembers_Degrees['BoardMembers_degree_school_role_company'] = BoardMembers_degree_school_role_company
        Company_BoardMembers_Degrees['BoardMembers_degree_school_role_investor'] = BoardMembers_degree_school_role_investor
        Company_BoardMembers_Degrees['BoardMembers_degree_school_role_group'] = BoardMembers_degree_school_role_group
        Company_BoardMembers_Degrees['BoardMembers_degree_school_role_school'] = BoardMembers_degree_school_role_school
        Company_BoardMembers_Degrees['BoardMembers_degree_school_investor_type'] = BoardMembers_degree_school_investor_type
        Company_BoardMembers_Degrees['BoardMembers_degree_school_founded_on'] = BoardMembers_degree_school_founded_on
        Company_BoardMembers_Degrees['BoardMembers_degree_school_founded_on_trust_code'] = BoardMembers_degree_school_founded_on_trust_code
        Company_BoardMembers_Degrees['BoardMembers_degree_school_is_closed'] = BoardMembers_degree_school_is_closed
        Company_BoardMembers_Degrees['BoardMembers_degree_school_closed_on'] = BoardMembers_degree_school_closed_on
        Company_BoardMembers_Degrees['BoardMembers_degree_school_closed_on_trust_code'] = BoardMembers_degree_school_closed_on_trust_code
        Company_BoardMembers_Degrees['BoardMembers_degree_school_num_employees_min'] = BoardMembers_degree_school_num_employees_min
        Company_BoardMembers_Degrees['BoardMembers_degree_school_num_employees_max'] = BoardMembers_degree_school_num_employees_max
        Company_BoardMembers_Degrees['BoardMembers_degree_school_stock_exchange'] = BoardMembers_degree_school_stock_exchange
        Company_BoardMembers_Degrees['BoardMembers_degree_school_stock_symbol'] = BoardMembers_degree_school_stock_symbol
        Company_BoardMembers_Degrees['BoardMembers_degree_school_total_funding_usd'] = BoardMembers_degree_school_total_funding_usd
        Company_BoardMembers_Degrees['BoardMembers_degree_school_number_of_investments'] = BoardMembers_degree_school_number_of_investments
        Company_BoardMembers_Degrees['BoardMembers_degree_school_homepage_url'] = BoardMembers_degree_school_homepage_url
        Company_BoardMembers_Degrees['BoardMembers_degree_school_contact_email'] = BoardMembers_degree_school_contact_email
        Company_BoardMembers_Degrees['BoardMembers_degree_school_phone_number'] = BoardMembers_degree_school_phone_number
        Company_BoardMembers_Degrees['BoardMembers_degree_school_rank'] = BoardMembers_degree_school_rank
        Company_BoardMembers_Degrees['BoardMembers_degree_school_created_at'] = BoardMembers_degree_school_created_at
        Company_BoardMembers_Degrees['BoardMembers_degree_school_updated_at'] = BoardMembers_degree_school_updated_at
        
        # Output data frame for CompanyBoardMembers_Jobs
        Company_BoardMembers_Jobs['company_uuid'] = company_uuid_BoardMembers_job
        Company_BoardMembers_Jobs['company_name'] = company_name_BoardMembers_job
        Company_BoardMembers_Jobs['BoardMembers_uuid'] = BoardMembers_uuid_BoardMembers_job
        Company_BoardMembers_Jobs['BoardMembers_first_name'] = BoardMembers_first_name_BoardMembers_job
        Company_BoardMembers_Jobs['BoardMembers_last_name'] = BoardMembers_last_name_BoardMembers_job
        Company_BoardMembers_Jobs['BoardMembers_job_type'] = BoardMembers_job_type
        Company_BoardMembers_Jobs['BoardMembers_job_uuid'] = BoardMembers_job_uuid
        Company_BoardMembers_Jobs['BoardMembers_job_title'] = BoardMembers_job_title
        Company_BoardMembers_Jobs['BoardMembers_job_started_on'] = BoardMembers_job_started_on
        Company_BoardMembers_Jobs['BoardMembers_job_started_on_trust_code'] = BoardMembers_job_started_on_trust_code
        Company_BoardMembers_Jobs['BoardMembers_job_ended_on'] = BoardMembers_job_ended_on
        Company_BoardMembers_Jobs['BoardMembers_job_ended_on_trust_code'] = BoardMembers_job_ended_on_trust_code
        Company_BoardMembers_Jobs['BoardMembers_job_is_current'] = BoardMembers_job_is_current
        Company_BoardMembers_Jobs['BoardMembers_job_job_type'] = BoardMembers_job_job_type
        Company_BoardMembers_Jobs['BoardMembers_job_created_at'] = BoardMembers_job_created_at
        Company_BoardMembers_Jobs['BoardMembers_job_updated_at'] = BoardMembers_job_updated_at
        Company_BoardMembers_Jobs['BoardMembers_job_organization_type'] = BoardMembers_job_organization_type
        Company_BoardMembers_Jobs['BoardMembers_job_organization_uuid'] = BoardMembers_job_organization_uuid
        Company_BoardMembers_Jobs['BoardMembers_job_organization_permalink'] = BoardMembers_job_organization_permalink
        Company_BoardMembers_Jobs['BoardMembers_job_organization_permalink_aliases'] = BoardMembers_job_organization_permalink_aliases
        Company_BoardMembers_Jobs['BoardMembers_job_organization_api_path'] = BoardMembers_job_organization_api_path
        Company_BoardMembers_Jobs['BoardMembers_job_organization_web_path'] = BoardMembers_job_organization_web_path
        Company_BoardMembers_Jobs['BoardMembers_job_organization_api_url'] = BoardMembers_job_organization_api_url
        Company_BoardMembers_Jobs['BoardMembers_job_organization_name'] = BoardMembers_job_organization_name
        Company_BoardMembers_Jobs['BoardMembers_job_organization_also_known_as'] = BoardMembers_job_organization_also_known_as
        Company_BoardMembers_Jobs['BoardMembers_job_organization_short_description'] = BoardMembers_job_organization_short_description
        Company_BoardMembers_Jobs['BoardMembers_job_organization_description'] = BoardMembers_job_organization_description
        Company_BoardMembers_Jobs['BoardMembers_job_organization_profile_image_url'] = BoardMembers_job_organization_profile_image_url
        Company_BoardMembers_Jobs['BoardMembers_job_organization_primary_role'] = BoardMembers_job_organization_primary_role
        Company_BoardMembers_Jobs['BoardMembers_job_organization_role_company'] = BoardMembers_job_organization_role_company
        Company_BoardMembers_Jobs['BoardMembers_job_organization_role_investor'] = BoardMembers_job_organization_role_investor
        Company_BoardMembers_Jobs['BoardMembers_job_organization_role_group'] = BoardMembers_job_organization_role_group
        Company_BoardMembers_Jobs['BoardMembers_job_organization_role_school'] = BoardMembers_job_organization_role_school
        Company_BoardMembers_Jobs['BoardMembers_job_organization_investor_type'] = BoardMembers_job_organization_investor_type
        Company_BoardMembers_Jobs['BoardMembers_job_organization_founded_on'] = BoardMembers_job_organization_founded_on
        Company_BoardMembers_Jobs['BoardMembers_job_organization_founded_on_trust_code'] = BoardMembers_job_organization_founded_on_trust_code
        Company_BoardMembers_Jobs['BoardMembers_job_organization_is_closed'] = BoardMembers_job_organization_is_closed
        Company_BoardMembers_Jobs['BoardMembers_job_organization_closed_on'] = BoardMembers_job_organization_closed_on
        Company_BoardMembers_Jobs['BoardMembers_job_organization_closed_on_trust_code'] = BoardMembers_job_organization_closed_on_trust_code
        Company_BoardMembers_Jobs['BoardMembers_job_organization_num_employees_min'] = BoardMembers_job_organization_num_employees_min
        Company_BoardMembers_Jobs['BoardMembers_job_organization_num_employees_max'] = BoardMembers_job_organization_num_employees_max
        Company_BoardMembers_Jobs['BoardMembers_job_organization_stock_exchange'] = BoardMembers_job_organization_stock_exchange
        Company_BoardMembers_Jobs['BoardMembers_job_organization_stock_symbol'] = BoardMembers_job_organization_stock_symbol
        Company_BoardMembers_Jobs['BoardMembers_job_organization_total_funding_usd'] = BoardMembers_job_organization_total_funding_usd
        Company_BoardMembers_Jobs['BoardMembers_job_organization_number_of_investments'] = BoardMembers_job_organization_number_of_investments
        Company_BoardMembers_Jobs['BoardMembers_job_organization_homepage_url'] = BoardMembers_job_organization_homepage_url
        Company_BoardMembers_Jobs['BoardMembers_job_organization_contact_email'] = BoardMembers_job_organization_contact_email
        Company_BoardMembers_Jobs['BoardMembers_job_organization_phone_number'] = BoardMembers_job_organization_phone_number
        Company_BoardMembers_Jobs['BoardMembers_job_organization_rank'] = BoardMembers_job_organization_rank
        Company_BoardMembers_Jobs['BoardMembers_job_organization_created_at'] = BoardMembers_job_organization_created_at
        Company_BoardMembers_Jobs['BoardMembers_job_organization_updated_at'] = BoardMembers_job_organization_updated_at
        
        # Output data frame for CompanyBoardMembers_FoundedCompanies
        Company_BoardMembers_FoundedCompanies['company_uuid'] = company_uuid_BoardMembers_founded_company
        Company_BoardMembers_FoundedCompanies['company_name'] = company_name_BoardMembers_founded_company
        Company_BoardMembers_FoundedCompanies['BoardMembers_uuid'] = BoardMembers_uuid_BoardMembers_founded_company
        Company_BoardMembers_FoundedCompanies['BoardMembers_first_name'] = BoardMembers_first_name_BoardMembers_founded_company
        Company_BoardMembers_FoundedCompanies['BoardMembers_last_name'] = BoardMembers_last_name_BoardMembers_founded_company
        Company_BoardMembers_FoundedCompanies['BoardMembers_founded_company_type'] = BoardMembers_founded_company_type
        Company_BoardMembers_FoundedCompanies['BoardMembers_founded_company_uuid'] = BoardMembers_founded_company_uuid
        Company_BoardMembers_FoundedCompanies['BoardMembers_founded_company_permalink'] = BoardMembers_founded_company_permalink
        Company_BoardMembers_FoundedCompanies['BoardMembers_founded_company_permalink_aliases'] = BoardMembers_founded_company_permalink_aliases
        Company_BoardMembers_FoundedCompanies['BoardMembers_founded_company_api_path'] = BoardMembers_founded_company_api_path
        Company_BoardMembers_FoundedCompanies['BoardMembers_founded_company_web_path'] = BoardMembers_founded_company_web_path
        Company_BoardMembers_FoundedCompanies['BoardMembers_founded_company_api_url'] = BoardMembers_founded_company_api_url
        Company_BoardMembers_FoundedCompanies['BoardMembers_founded_company_name'] = BoardMembers_founded_company_name
        Company_BoardMembers_FoundedCompanies['BoardMembers_founded_company_also_known_as'] = BoardMembers_founded_company_also_known_as
        Company_BoardMembers_FoundedCompanies['BoardMembers_founded_company_short_description'] = BoardMembers_founded_company_short_description
        Company_BoardMembers_FoundedCompanies['BoardMembers_founded_company_description'] = BoardMembers_founded_company_description
        Company_BoardMembers_FoundedCompanies['BoardMembers_founded_company_profile_image_url'] = BoardMembers_founded_company_profile_image_url
        Company_BoardMembers_FoundedCompanies['BoardMembers_founded_company_primary_role'] = BoardMembers_founded_company_primary_role
        Company_BoardMembers_FoundedCompanies['BoardMembers_founded_company_role_company'] = BoardMembers_founded_company_role_company
        Company_BoardMembers_FoundedCompanies['BoardMembers_founded_company_role_investor'] = BoardMembers_founded_company_role_investor
        Company_BoardMembers_FoundedCompanies['BoardMembers_founded_company_role_group'] = BoardMembers_founded_company_role_group
        Company_BoardMembers_FoundedCompanies['BoardMembers_founded_company_role_school'] = BoardMembers_founded_company_role_school
        Company_BoardMembers_FoundedCompanies['BoardMembers_founded_company_investor_type'] = BoardMembers_founded_company_investor_type
        Company_BoardMembers_FoundedCompanies['BoardMembers_founded_company_founded_on'] = BoardMembers_founded_company_founded_on
        Company_BoardMembers_FoundedCompanies['BoardMembers_founded_company_founded_on_trust_code'] = BoardMembers_founded_company_founded_on_trust_code
        Company_BoardMembers_FoundedCompanies['BoardMembers_founded_company_is_closed'] = BoardMembers_founded_company_is_closed
        Company_BoardMembers_FoundedCompanies['BoardMembers_founded_company_closed_on'] = BoardMembers_founded_company_closed_on
        Company_BoardMembers_FoundedCompanies['BoardMembers_founded_company_closed_on_trust_code'] = BoardMembers_founded_company_closed_on_trust_code
        Company_BoardMembers_FoundedCompanies['BoardMembers_founded_company_num_employees_min'] = BoardMembers_founded_company_num_employees_min
        Company_BoardMembers_FoundedCompanies['BoardMembers_founded_company_num_employees_max'] = BoardMembers_founded_company_num_employees_max
        Company_BoardMembers_FoundedCompanies['BoardMembers_founded_company_stock_exchange'] = BoardMembers_founded_company_stock_exchange
        Company_BoardMembers_FoundedCompanies['BoardMembers_founded_company_stock_symbol'] = BoardMembers_founded_company_stock_symbol
        Company_BoardMembers_FoundedCompanies['BoardMembers_founded_company_total_funding_usd'] = BoardMembers_founded_company_total_funding_usd
        Company_BoardMembers_FoundedCompanies['BoardMembers_founded_company_number_of_investments'] = BoardMembers_founded_company_number_of_investments
        Company_BoardMembers_FoundedCompanies['BoardMembers_founded_company_homepage_url'] = BoardMembers_founded_company_homepage_url
        Company_BoardMembers_FoundedCompanies['BoardMembers_founded_company_contact_email'] = BoardMembers_founded_company_contact_email
        Company_BoardMembers_FoundedCompanies['BoardMembers_founded_company_phone_number'] = BoardMembers_founded_company_phone_number
        Company_BoardMembers_FoundedCompanies['BoardMembers_founded_company_rank'] = BoardMembers_founded_company_rank
        Company_BoardMembers_FoundedCompanies['BoardMembers_founded_company_created_at'] = BoardMembers_founded_company_created_at
        Company_BoardMembers_FoundedCompanies['BoardMembers_founded_company_updated_at'] = BoardMembers_founded_company_updated_at   
        
        # Output data frame for CompanyBoardMembers_Websites
        Company_BoardMembers_Websites['company_uuid'] = company_uuid_BoardMembers_website
        Company_BoardMembers_Websites['company_name'] = company_name_BoardMembers_website
        Company_BoardMembers_Websites['BoardMembers_uuid'] = BoardMembers_uuid_BoardMembers_website
        Company_BoardMembers_Websites['BoardMembers_first_name'] =  BoardMembers_first_name_BoardMembers_website
        Company_BoardMembers_Websites['BoardMembers_last_name'] = BoardMembers_last_name_BoardMembers_website
        Company_BoardMembers_Websites['BoardMembers_website_type'] = BoardMembers_website_type
        Company_BoardMembers_Websites['BoardMembers_website_uuid'] = BoardMembers_website_uuid
        Company_BoardMembers_Websites['BoardMembers_website_website_type'] = BoardMembers_website_website_type
        Company_BoardMembers_Websites['BoardMembers_website_website_name'] = BoardMembers_website_website_name
        Company_BoardMembers_Websites['BoardMembers_website_url'] = BoardMembers_website_url
        Company_BoardMembers_Websites['BoardMembers_website_created_at'] = BoardMembers_website_created_at
        Company_BoardMembers_Websites['BoardMembers_website_updated_at'] = BoardMembers_website_updated_at
        
        Company_BoardMembers_AdvisoryRoles['company_uuid'] = company_uuid_BoardMembers_advisory_role
        Company_BoardMembers_AdvisoryRoles['company_name'] = company_name_BoardMembers_advisory_role
        Company_BoardMembers_AdvisoryRoles['BoardMembers_uuid'] = BoardMembers_uuid_BoardMembers_advisory_role
        Company_BoardMembers_AdvisoryRoles['BoardMembers_first_name'] = BoardMembers_first_name_BoardMembers_advisory_role
        Company_BoardMembers_AdvisoryRoles['BoardMembers_last_name'] = BoardMembers_last_name_BoardMembers_advisory_role
        Company_BoardMembers_AdvisoryRoles['BoardMembers_advisory_role_type'] = BoardMembers_advisory_role_type
        Company_BoardMembers_AdvisoryRoles['BoardMembers_advisory_role_uuid'] = BoardMembers_advisory_role_uuid
        Company_BoardMembers_AdvisoryRoles['BoardMembers_advisory_role_title'] = BoardMembers_advisory_role_title
        Company_BoardMembers_AdvisoryRoles['BoardMembers_advisory_role_started_on'] = BoardMembers_advisory_role_started_on
        Company_BoardMembers_AdvisoryRoles['BoardMembers_advisory_role_started_on_trust_code'] = BoardMembers_advisory_role_started_on_trust_code
        Company_BoardMembers_AdvisoryRoles['BoardMembers_advisory_role_ended_on'] = BoardMembers_advisory_role_ended_on
        Company_BoardMembers_AdvisoryRoles['BoardMembers_advisory_role_ended_on_trust_code'] = BoardMembers_advisory_role_ended_on_trust_code
        Company_BoardMembers_AdvisoryRoles['BoardMembers_advisory_role_is_current'] = BoardMembers_advisory_role_is_current
        Company_BoardMembers_AdvisoryRoles['BoardMembers_advisory_role_job_type'] = BoardMembers_advisory_role_job_type
        Company_BoardMembers_AdvisoryRoles['BoardMembers_advisory_role_created_at'] = BoardMembers_advisory_role_created_at
        Company_BoardMembers_AdvisoryRoles['BoardMembers_advisory_role_updated_at'] = BoardMembers_advisory_role_updated_at
        Company_BoardMembers_AdvisoryRoles['BoardMembers_advisory_role_organization_permalink'] = BoardMembers_advisory_role_organization_permalink
        Company_BoardMembers_AdvisoryRoles['BoardMembers_advisory_role_organization_permalink_aliases'] = BoardMembers_advisory_role_organization_permalink_aliases
        Company_BoardMembers_AdvisoryRoles['BoardMembers_advisory_role_organization_api_path'] = BoardMembers_advisory_role_organization_api_path
        Company_BoardMembers_AdvisoryRoles['BoardMembers_advisory_role_organization_web_path'] = BoardMembers_advisory_role_organization_web_path
        Company_BoardMembers_AdvisoryRoles['BoardMembers_advisory_role_organization_api_url'] = BoardMembers_advisory_role_organization_api_url
        Company_BoardMembers_AdvisoryRoles['BoardMembers_advisory_role_organization_name'] = BoardMembers_advisory_role_organization_name
        Company_BoardMembers_AdvisoryRoles['BoardMembers_advisory_role_organization_also_known_as'] = BoardMembers_advisory_role_organization_also_known_as
        Company_BoardMembers_AdvisoryRoles['BoardMembers_advisory_role_organization_short_description'] = BoardMembers_advisory_role_organization_short_description
        Company_BoardMembers_AdvisoryRoles['BoardMembers_advisory_role_organization_description'] = BoardMembers_advisory_role_organization_description
        Company_BoardMembers_AdvisoryRoles['BoardMembers_advisory_role_organization_profile_image_url'] = BoardMembers_advisory_role_organization_profile_image_url
        Company_BoardMembers_AdvisoryRoles['BoardMembers_advisory_role_organization_primary_role'] = BoardMembers_advisory_role_organization_primary_role
        Company_BoardMembers_AdvisoryRoles['BoardMembers_advisory_role_organization_role_company'] = BoardMembers_advisory_role_organization_role_company
        Company_BoardMembers_AdvisoryRoles['BoardMembers_advisory_role_organization_role_investor'] = BoardMembers_advisory_role_organization_role_investor
        Company_BoardMembers_AdvisoryRoles['BoardMembers_advisory_role_organization_role_group'] = BoardMembers_advisory_role_organization_role_group
        Company_BoardMembers_AdvisoryRoles['BoardMembers_advisory_role_organization_role_school'] = BoardMembers_advisory_role_organization_role_school
        Company_BoardMembers_AdvisoryRoles['BoardMembers_advisory_role_organization_investor_type'] = BoardMembers_advisory_role_organization_investor_type
        Company_BoardMembers_AdvisoryRoles['BoardMembers_advisory_role_organization_founded_on'] = BoardMembers_advisory_role_organization_founded_on
        Company_BoardMembers_AdvisoryRoles['BoardMembers_advisory_role_organization_founded_on_trust_code'] = BoardMembers_advisory_role_organization_founded_on_trust_code
        Company_BoardMembers_AdvisoryRoles['BoardMembers_advisory_role_organization_is_closed'] = BoardMembers_advisory_role_organization_is_closed
        Company_BoardMembers_AdvisoryRoles['BoardMembers_advisory_role_organization_closed_on'] = BoardMembers_advisory_role_organization_closed_on
        Company_BoardMembers_AdvisoryRoles['BoardMembers_advisory_role_organization_closed_on_trust_code'] = BoardMembers_advisory_role_organization_closed_on_trust_code
        Company_BoardMembers_AdvisoryRoles['BoardMembers_advisory_role_organization_num_employees_min'] = BoardMembers_advisory_role_organization_num_employees_min
        Company_BoardMembers_AdvisoryRoles['BoardMembers_advisory_role_organization_num_employees_max'] = BoardMembers_advisory_role_organization_num_employees_max
        Company_BoardMembers_AdvisoryRoles['BoardMembers_advisory_role_organization_stock_exchange'] = BoardMembers_advisory_role_organization_stock_exchange
        Company_BoardMembers_AdvisoryRoles['BoardMembers_advisory_role_organization_stock_symbol'] = BoardMembers_advisory_role_organization_stock_symbol
        Company_BoardMembers_AdvisoryRoles['BoardMembers_advisory_role_organization_total_funding_usd'] = BoardMembers_advisory_role_organization_total_funding_usd
        Company_BoardMembers_AdvisoryRoles['BoardMembers_advisory_role_organization_number_of_investments'] = BoardMembers_advisory_role_organization_number_of_investments
        Company_BoardMembers_AdvisoryRoles['BoardMembers_advisory_role_organization_homepage_url'] = BoardMembers_advisory_role_organization_homepage_url
        Company_BoardMembers_AdvisoryRoles['BoardMembers_advisory_role_organization_contact_email'] = BoardMembers_advisory_role_organization_contact_email
        Company_BoardMembers_AdvisoryRoles['BoardMembers_advisory_role_organization_phone_number'] = BoardMembers_advisory_role_organization_phone_number
        Company_BoardMembers_AdvisoryRoles['BoardMembers_advisory_role_organization_rank'] = BoardMembers_advisory_role_organization_rank
        Company_BoardMembers_AdvisoryRoles['BoardMembers_advisory_role_organization_created_at'] = BoardMembers_advisory_role_organization_created_at
        Company_BoardMembers_AdvisoryRoles['BoardMembers_advisory_role_organization_updated_at'] = BoardMembers_advisory_role_organization_updated_at
        
        Company_BoardMembers_Investments['company_uuid'] = company_uuid_BoardMembers_investments
        Company_BoardMembers_Investments['company_name'] = company_name_BoardMembers_investments
        Company_BoardMembers_Investments['BoardMembers_uuid'] = BoardMembers_uuid_BoardMembers_investments
        Company_BoardMembers_Investments['BoardMembers_first_name'] = BoardMembers_first_name_investments
        Company_BoardMembers_Investments['BoardMembers_last_name'] = BoardMembers_last_name_BoardMembers_investments
        Company_BoardMembers_Investments['BoardMembers_investment_type'] = BoardMembers_investment_type
        Company_BoardMembers_Investments['BoardMembers_investment_uuid'] = BoardMembers_investment_uuid
        Company_BoardMembers_Investments['BoardMembers_investment_money_invested'] = BoardMembers_investment_money_invested
        Company_BoardMembers_Investments['BoardMembers_investment_money_invested_currency_code'] = BoardMembers_investment_money_invested_currency_code
        Company_BoardMembers_Investments['BoardMembers_investment_money_invested_usd'] = BoardMembers_investment_money_invested_usd
        Company_BoardMembers_Investments['BoardMembers_investment_is_lead_investor'] = BoardMembers_investment_is_lead_investor
        Company_BoardMembers_Investments['BoardMembers_investment_announced_on'] = BoardMembers_investment_announced_on
        Company_BoardMembers_Investments['BoardMembers_investment_announced_on_trust_code'] = BoardMembers_investment_announced_on_trust_code
        Company_BoardMembers_Investments['BoardMembers_investment_created_at'] = BoardMembers_investment_created_at
        Company_BoardMembers_Investments['BoardMembers_investment_updated_at'] = BoardMembers_investment_updated_at
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_type'] = BoardMembers_investment_funding_round_type
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_uuid'] = BoardMembers_investment_funding_round_uuid
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_permalink'] = BoardMembers_investment_funding_round_permalink
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_api_path'] = BoardMembers_investment_funding_round_api_path
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_web_path'] = BoardMembers_investment_funding_round_web_path
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_api_url'] = BoardMembers_investment_funding_round_api_url
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_funding_type'] = BoardMembers_investment_funding_round_funding_type
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_series'] = BoardMembers_investment_funding_round_series
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_series_qualifier'] = BoardMembers_investment_funding_round_series_qualifier
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_announced_on'] = BoardMembers_investment_funding_round_announced_on
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_announced_on_trust_code'] = BoardMembers_investment_funding_round_announced_on_trust_code
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_closed_on'] = BoardMembers_investment_funding_round_closed_on
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_closed_on_trust_code'] = BoardMembers_investment_funding_round_closed_on_trust_code
        Company_BoardMembers_Investments['BoardMembers_investment_funding_money_raised'] = BoardMembers_investment_funding_money_raised
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_money_raised_currency_code'] = BoardMembers_investment_funding_round_money_raised_currency_code
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_money_raised_usd'] = BoardMembers_investment_funding_round_money_raised_usd
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_target_money_raised'] = BoardMembers_investment_funding_round_target_money_raised
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_target_money_raised_currency_code'] = BoardMembers_investment_funding_round_target_money_raised_currency_code
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_target_money_raised_usd'] = BoardMembers_investment_funding_round_target_money_raised_usd
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_pre_money_valuation'] = BoardMembers_investment_funding_round_pre_money_valuation
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_pre_money_valuation_currency_code'] = BoardMembers_investment_funding_round_pre_money_valuation_currency_code
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_pre_money_valuation_usd'] = BoardMembers_investment_funding_round_pre_money_valuation_usd
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_rank'] = BoardMembers_investment_funding_round_rank
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_created_at'] = BoardMembers_investment_funding_round_created_at
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_updated_at'] = BoardMembers_investment_funding_round_updated_at
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_funded_organization_type'] = BoardMembers_investment_funding_round_funded_organization_type
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_funded_organization_uuid'] = BoardMembers_investment_funding_round_funded_organization_uuid
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_funded_organization_permalink'] = BoardMembers_investment_funding_round_funded_organization_permalink
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_funded_organization_permalink_aliases'] = BoardMembers_investment_funding_round_funded_organization_permalink_aliases
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_funded_organization_api_path'] = BoardMembers_investment_funding_round_funded_organization_api_path
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_funded_organization_web_path'] = BoardMembers_investment_funding_round_funded_organization_web_path
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_funded_organization_api_url'] = BoardMembers_investment_funding_round_funded_organization_api_url
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_funded_organization_name'] = BoardMembers_investment_funding_round_funded_organization_name
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_funded_organization_also_known_as'] = BoardMembers_investment_funding_round_funded_organization_also_known_as
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_funded_organization_short_description'] = BoardMembers_investment_funding_round_funded_organization_short_description
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_funded_organization_description'] = BoardMembers_investment_funding_round_funded_organization_description
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_funded_organization_profile_image_url'] = BoardMembers_investment_funding_round_funded_organization_profile_image_url
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_funded_organization_primary_role'] = BoardMembers_investment_funding_round_funded_organization_primary_role
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_funded_organization_role_company'] = BoardMembers_investment_funding_round_funded_organization_role_company
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_funded_organization_role_investor'] = BoardMembers_investment_funding_round_funded_organization_role_investor
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_funded_organization_role_group'] = BoardMembers_investment_funding_round_funded_organization_role_group
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_funded_organization_role_school'] = BoardMembers_investment_funding_round_funded_organization_role_school
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_funded_organization_investor_type'] = BoardMembers_investment_funding_round_funded_organization_investor_type
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_funded_organization_founded_on'] = BoardMembers_investment_funding_round_funded_organization_founded_on
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_funded_organization_founded_on_trust_code'] = BoardMembers_investment_funding_round_funded_organization_founded_on_trust_code
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_funded_organization_is_closed'] = BoardMembers_investment_funding_round_funded_organization_is_closed
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_funded_organization_closed_on'] = BoardMembers_investment_funding_round_funded_organization_closed_on
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_funded_organization_closed_on_trust_code'] = BoardMembers_investment_funding_round_funded_organization_closed_on_trust_code
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_funded_organization_num_employees_min'] = BoardMembers_investment_funding_round_funded_organization_num_employees_min
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_funded_organization_num_employees_max'] = BoardMembers_investment_funding_round_funded_organization_num_employees_max
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_funded_organization_stock_exchange'] = BoardMembers_investment_funding_round_funded_organization_stock_exchange
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_funded_organization_stock_symbol'] = BoardMembers_investment_funding_round_funded_organization_stock_symbol
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_funded_organization_total_funding_usd'] = BoardMembers_investment_funding_round_funded_organization_total_funding_usd
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_funded_organization_number_of_investments'] = BoardMembers_investment_funding_round_funded_organization_number_of_investments
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_funded_organization_homepage_url'] = BoardMembers_investment_funding_round_funded_organization_homepage_url
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_funded_organization_contact_email'] = BoardMembers_investment_funding_round_funded_organization_contact_email
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_funded_organization_phone_number'] = BoardMembers_investment_funding_round_funded_organization_phone_number
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_funded_organization_rank'] = BoardMembers_investment_funding_round_funded_organization_rank
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_funded_organization_created_at'] = BoardMembers_investment_funding_round_funded_organization_created_at
        Company_BoardMembers_Investments['BoardMembers_investment_funding_round_funded_organization_updated_at'] = BoardMembers_investment_funding_round_funded_organization_updated_at       
        
        # Output all data frames to csv after each company has been scraped

        Company_Details.to_csv(r'Company_Details_'+ folder_location_name +'.csv')
        Company_FundingRounds.to_csv(r'Company_FundingRounds_'+ folder_location_name +'.csv')
        Company_FundingRounds_Investors.to_csv(r'Company_FundingRounds_Investors_'+ folder_location_name +'.csv')
        Company_FundingRounds_Investors_Partners.to_csv(r'Company_FundingRounds_Investors_Partners_'+ folder_location_name +'.csv')
        Company_Acquisitions.to_csv(r'Company_Acquisitions_'+ folder_location_name +'.csv')
        Company_Offices.to_csv(r'Company_Offices_'+ folder_location_name +'.csv')
        Company_Headquarters.to_csv(r'Company_Headquarters_'+ folder_location_name +'.csv')
        Company_SubOrganizations.to_csv(r'Company_SubOrganizations_'+ folder_location_name +'.csv')
        Company_Founders.to_csv(r'Company_Founders_'+ folder_location_name +'.csv')
        Company_Founders_Degrees.to_csv(r'Company_Founders_Degrees_'+ folder_location_name +'.csv')
        Company_Founders_Jobs.to_csv(r'Company_Founders_Jobs_'+ folder_location_name +'.csv')
        Company_Founders_FoundedCompanies.to_csv(r'Company_Founders_FoundedCompanies_'+ folder_location_name +'.csv')
        Company_Founders_Websites.to_csv(r'Company_Founders_Websites_'+ folder_location_name +'.csv')
        Company_Founders_AdvisoryRoles.to_csv(r'Company_Founders_AdvisoryRoles_'+ folder_location_name +'.csv')
        Company_Founders_Investments.to_csv(r'Company_Founders_Investments_'+ folder_location_name +'.csv')
        Company_BoardMembers.to_csv(r'Company_BoardMembers_'+ folder_location_name +'.csv')
        Company_BoardMembers_Degrees.to_csv(r'Company_BoardMembers_Degrees_'+ folder_location_name +'.csv')
        Company_BoardMembers_Jobs.to_csv(r'Company_BoardMembers_Jobs_'+ folder_location_name +'.csv')
        Company_BoardMembers_FoundedCompanies.to_csv(r'Company_BoardMembers_FoundedCompanies_'+ folder_location_name +'.csv')
        Company_BoardMembers_Websites.to_csv(r'Company_BoardMembers_Websites_'+ folder_location_name +'.csv')
        Company_BoardMembers_AdvisoryRoles.to_csv(r'Company_BoardMembers_AdvisoryRoles_'+ folder_location_name +'.csv')
        Company_BoardMembers_Investments.to_csv(r'Company_BoardMembers_Investments_'+ folder_location_name +'.csv')

        
        # Tracking time taken for scraping
        company_end= time.time()
        company_scraping_time= company_end-company_start
        total_scraping_time_seconds= company_end-code_start
        total_scraping_time_minutes= int(total_scraping_time_seconds/60) - 60*int(total_scraping_time_seconds/3600)
        total_scraping_time_hours= int(total_scraping_time_seconds/3600)
        
        # Print scraping status
        print(('Scraping completed for {} companies').format(company_count))
        print(('Last company scraped was {} ').format(company_name[-1]))
        print(('Last company was scraped in {} seconds').format(company_scraping_time))
        print(('Total time taken for scraping {} companies is {} hours and {} minutes\n').format(company_count, total_scraping_time_hours, total_scraping_time_minutes))
        company_count +=1
    except:
        #print(('Scraping returned error for {} companies').format(company_count_error))
        #print('Last company that returned error while scraping was {} ').format(company_permalink_input)
        #Error['company_url']= company_url_error
        #Error.to_csv(r'Error.csv')
        
        Error=pd.DataFrame()
        company_count_error +=1
        company_url_error.append(company_url)
        Error['company_url']=company_url_error
        Error.to_csv(r'Error_'+ folder_location_name +'.csv')
        print(company_url)
        print('\n')
        time.sleep(2)
        continue
