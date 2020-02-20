#
# define types for omop schema
#
class ModelOmopPandas:
    #
    # Check the model matches
    #
    def __init__(self):
       self.model_schema = self.omopSchema()

    #
    # define omop schema here
    # The date fields are read in as string.  They can be converted to date
    # objects if necessary
    # OMOP V5.3.1
    #
    def omopSchema(self):
        model_schema = {}
        #
        # Standardized vocabulary
        #
        model_schema['concept'] = {
            'concept_id': 'int64',
            'concept_name': 'object',
            'domain_id': 'category',
            'vocabulary_id': 'category',
            'concept_class_id': 'category',
            'standard_concept': 'category',
            'concept_code': 'category',
            'valid_start_date': 'object',
            'valid_end_date': 'object',
            'invalid_reason': 'category'
        }

        model_schema['vocabulary'] = {
            'vocabulary_id': 'object',
            'vocabulary_name': 'category',
            'vocabulary_reference': 'category',
            'vocabulary_version': 'category',
            'vocabulary_concept_id': 'int64'
        }

        model_schema['domain'] = {
            'domain_id': 'category',
            'domain_name': 'category',
            'domain_concept_id': 'int64'
        }

        model_schema['concept_class'] = {
            'concept_class_id': 'category',
            'concept_class_name': 'category',
            'concept_class_concept_id': 'int64'
        }

        model_schema['concept_relationship'] = {
            'concept_id_1': 'int64',
            'concept_id_2': 'int64',
            'relationship_id': 'category',
            'valid_start_date': 'object',
            'valid_end_date': 'object',
            'invalid_reason': 'category'
        }

        model_schema['relationship'] = {
            'relationship_id': 'object',
            'relationship_name': 'category',
            'is_hierarchical': 'category',
            'defines_ancestry': 'category',
            'reverse_relationship_id': 'category',
            'relationship_concept_id': 'int64'  
        }

        model_schema['concept_synonym'] = {
            'concept_id': 'int64',
            'concept_synonym_name': 'category',
            'language_concept_id': 'int64'
        }

        model_schema['concept_ancestor'] = {
            'ancestor_concept_id': 'int64',
            'descendant_concept_id': 'int64',
            'min_levels_of_separation':'int64',
            'max_levels_of_separation':'int64'
        }

        model_schema['source_to_concept_map'] = {
            'source_code': 'category',
            'source_concept_id': 'int64',
            'source_vocabulary_id': 'category',
            'source_code_description': 'category',
            'target_concept_id': 'int64',
            'target_vocabulary_id': 'category',
            'valid_start_date':'object',
            'valid_end_date': 'object',
            'invalid_reason': 'category'
        }

        model_schema['drug_strength'] = {
            'drug_concept_id': 'int64',
            'ingredient_concept_id': 'int64',
            'amount_value': 'float',
            'amount_unit_concept_id': 'int64',
            'numerator_value': 'float' ,
            'numerator_unit_concept_id': 'int64',
            'denominator_value': 'float' ,
            'denominator_unit_concept_id': 'int64',
            'box_size': 'int64',
            'valid_start_date': 'object',
            'valid_end_date': 'object',
            'invalid_reason': 'category'
        }

        model_schema['cohort_definition'] = {
            'cohort_definition_id': 'int64',
            'cohort_definition_name': 'category',
            'cohort_definition_description': 'object',
            'definition_type_concept_id': 'int64',
            'cohort_definition_syntax': 'object',
            'subject_concept_id': 'int64',
            'cohort_initiation_date':'object'    
        }

        model_schema['attribute_definition'] = {
            'attribute_definition_id': 'int64',
            'attribute_name': 'category',
            'attribute_description':  'object',
            'attribute_type_concept_id': 'int64',
            'attribute_syntax': 'object'
        }

        # Standardized meta-data
        model_schema['cdm_source'] = {
            'cdm_source_name': 'category',
            'cdm_source_abbreviation': 'category',
            'cdm_holder': 'category',
            'source_description': 'object',
            'source_documentation_reference': 'category',
            'cdm_etl_reference': 'category',
            'source_release_date': 'object',
            'cdm_release_date': 'object',
            'cdm_version': 'category',
            'vocabulary_version': 'category'
        }

        model_schema['metadata'] = {
            'metadata_concept_id': 'int64',
            'metadata_type_concept_id': 'int64',
            'name': 'category',
            'value_as_string': 'object',
            'value_as_concept_id': 'int64',
            'metadata_date': 'object',
            'metadata_datetime': 'object'      
        }

        # Standardized clinical data
        model_schema['person'] = {
            'person_id': 'int64',
            'gender_concept_id': 'int64',
            'year_of_birth': 'int64',
            'month_of_birth': 'int64',
            'day_of_birth': 'int64',
            'birth_datetime': 'object',
            'race_concept_id': 'int64',
            'ethnicity_concept_id': 'int64',
            'location_id': 'int64',
            'provider_id': 'int64',
            'care_site_id': 'int64',
            'person_source_value': 'category',
            'gender_source_value': 'category',
            'gender_source_concept_id': 'int64',
            'race_source_value': 'category',
            'race_source_concept_id': 'int64',
            'ethnicity_source_value': 'category',
            'ethnicity_source_concept_id': 'int64'  
        }

        model_schema['observation_period'] = {
            'observation_period_id': 'int64',
            'person_id': 'int64',
            'observation_period_start_date': 'object',
            'observation_period_end_date': 'object',
            'period_type_concept_id': 'int64'
        }

        model_schema['specimen'] = {
            'specimen_id': 'int64',
            'person_id': 'int64',
            'specimen_concept_id': 'int64',
            'specimen_type_concept_id': 'int64',
            'specimen_date': 'object',
            'specimen_datetime':  'object',
            'quantity': 'float',
            'unit_concept_id': 'int64',
            'anatomic_site_concept_id': 'int64',
            'disease_status_concept_id': 'int64',
            'specimen_source_id': 'category',
            'specimen_source_value': 'category',
            'unit_source_value': 'category',
            'anatomic_site_source_value': 'category',
            'disease_status_source_value': 'category'
        }

        model_schema['death'] = {
            'person_id': 'int64',
            'death_date': 'object',
            'death_datetime': 'object',
            'death_type_concept_id': 'int64',
            'cause_concept_id': 'int64',
            'cause_source_value': 'category',
            'cause_source_concept_id': 'int64'
        }

        model_schema['visit_occurrence'] = {
            'visit_occurrence_id': 'int64',
            'person_id': 'int64',
            'visit_concept_id': 'int64',
            'visit_start_date': 'object',
            'visit_start_datetime': 'object',
            'visit_end_date': 'object',
            'visit_end_datetime': 'object',
            'visit_type_concept_id': 'int64',
            'provider_id': 'int64',
            'care_site_id': 'int64',
            'visit_source_value': 'category',
            'visit_source_concept_id': 'int64',
            'admitting_source_concept_id': 'int64',
            'admitting_source_value': 'category',
            'discharge_to_concept_id': 'int64' ,
            'discharge_to_source_value': 'category',
            'preceding_visit_occurrence_id': 'int64'
        }     

        model_schema['visit_detail'] = {
            'visit_detail_id': 'int64',
            'person_id': 'int64',
            'visit_detail_concept_id': 'int64',
            'visit_detail_start_date': 'object',
            'visit_detail_start_datetime': 'object',
            'visit_detail_end_date': 'object'   ,
            'visit_detail_end_datetime': 'object',
            'visit_detail_type_concept_id': 'int64',
            'provider_id': 'int64',
            'care_site_id': 'int64',
            'admitting_source_concept_id': 'int64',
            'discharge_to_concept_id': 'int64',
            'preceding_visit_detail_id': 'int64',
            'visit_detail_source_value': 'category',
            'visit_detail_source_concept_id': 'int64',
            'admitting_source_value': 'category',
            'discharge_to_source_value': 'category',
            'visit_detail_parent_id': 'int64',
            'visit_occurrence_id': 'int64'     
        }    

        model_schema['procedure_occurrence'] = {
            'procedure_occurrence_id': 'int64',
            'person_id': 'int64',
            'procedure_concept_id': 'int64',
            'procedure_date': 'object',
            'procedure_datetime': 'object',
            'procedure_type_concept_id': 'int64',
            'modifier_concept_id': 'int64',
            'quantity': 'int64',
            'provider_id': 'int64',
            'visit_occurrence_id': 'int64',
            'visit_detail_id': 'int64',
            'procedure_source_value': 'category',
            'procedure_source_concept_id': 'int64',
            'modifier_source_value': 'category'
        }

        model_schema['drug_exposure'] = {
            'drug_exposure_id': 'int64',
            'person_id': 'int64',
            'drug_concept_id': 'int64',
            'drug_exposure_start_date': 'object',
            'drug_exposure_start_datetime': 'object',
            'drug_exposure_end_date': 'object',
            'drug_exposure_end_datetime': 'object',
            'verbatim_end_date': 'object'  ,
            'drug_type_concept_id': 'int64',
            'stop_reason': 'category',
            'refills': 'int64',
            'quantity': 'float',
            'days_supply': 'int64',
            'sig': 'object',
            'route_concept_id': 'int64',
            'lot_number': 'category',
            'provider_id': 'int64',
            'visit_occurrence_id': 'int64',
            'visit_detail_id': 'int64',
            'drug_source_value': 'category',
            'drug_source_concept_id': 'int64',
            'route_source_value': 'category',
            'dose_unit_source_value': 'category'  
        }

        model_schema['device_exposure'] = {
            'device_exposure_id': 'int64',
            'person_id': 'int64',
            'device_concept_id': 'int64',
            'device_exposure_start_date': 'object',
            'device_exposure_start_datetime': 'object',
            'device_exposure_end_date': 'object',
            'device_exposure_end_datetime': 'object',
            'device_type_concept_id': 'int64',
            'unique_device_id': 'category',
            'quantity': 'int64',
            'provider_id': 'int64',
            'visit_occurrence_id': 'int64',
            'visit_detail_id': 'int64',
            'device_source_value': 'category',
            'device_source_concept_id': 'int64'  
        }

        model_schema['condition_occurrence'] = {
            'condition_occurrence_id': 'int64',
            'person_id': 'int64',
            'condition_concept_id': 'int64',
            'condition_start_date': 'object',
            'condition_start_datetime': 'object',
            'condition_end_date': 'object',
            'condition_end_datetime': 'object',
            'condition_type_concept_id': 'int64',
            'stop_reason': 'category',
            'provider_id': 'int64',
            'visit_occurrence_id': 'int64',
            'visit_detail_id': 'int64',
            'condition_source_value': 'category',
            'condition_source_concept_id': 'int64',
            'condition_status_source_value': 'category',
            'condition_status_concept_id': 'int64'
        }

        model_schema['measurement'] = {
            'measurement_id': 'int64',
            'person_id': 'int64',
            'measurement_concept_id': 'int64',
            'measurement_date': 'object',
            'measurement_datetime': 'object',
            'measurement_time': 'category',
            'measurement_type_concept_id': 'int64',
            'operator_concept_id': 'int64',
            'value_as_number': 'float',
            'value_as_concept_id': 'int64',
            'unit_concept_id': 'int64',
            'range_low': 'float',
            'range_high': 'float',
            'provider_id': 'int64',
            'visit_occurrence_id': 'int64',
            'visit_detail_id': 'int64',
            'measurement_source_value':  'category',
            'measurement_source_concept_id': 'int64',
            'unit_source_value': 'category',
            'value_source_value': 'category'
        }

        model_schema['note'] = {
            'note_id': 'int64',
            'person_id': 'int64',
            'note_date': 'object'  ,
            'note_datetime': 'object',
            'note_type_concept_id': 'int64',
            'note_class_concept_id': 'int64',
            'note_title': 'category',
            'note_text': 'object',
            'encoding_concept_id': 'int64',
            'language_concept_id': 'int64',
            'provider_id': 'int64',
            'visit_occurrence_id': 'int64',
            'visit_detail_id': 'int64',
            'note_source_value': 'category'
        }

        model_schema['note_nlp'] = {
            'note_nlp_id': 'int64',
            'note_id': 'int64',
            'section_concept_id': 'int64',
            'snippet': 'category',
            'offset': 'category',
            'lexical_variant': 'category',
            'note_nlp_concept_id': 'int64',
            'note_nlp_source_concept_id': 'int64',
            'nlp_system': 'category',
            'nlp_date': 'object',
            'nlp_datetime': 'object',
            'term_exists': 'category',
            'term_temporal': 'category',
            'term_modifiers': 'category'
        }

        model_schema['observation'] = {
            'observation_id': 'int64',
            'person_id': 'int64',
            'observation_concept_id': 'int64',
            'observation_date': 'object',
            'observation_datetime': 'object',
            'observation_type_concept_id': 'int64',
            'value_as_number': 'float',
            'value_as_string': 'category',
            'value_as_concept_id': 'int64',
            'qualifier_concept_id': 'int64',
            'unit_concept_id': 'int64',
            'provider_id': 'int64',
            'visit_occurrence_id': 'int64',
            'visit_detail_id': 'int64',
            'observation_source_value': 'category',
            'observation_source_concept_id': 'int64',
            'unit_source_value': 'category',
            'qualifier_source_value': 'category'
        }

        model_schema['fact_relationship'] = {
            'domain_concept_id_1': 'int64',
            'fact_id_1': 'int64',
            'domain_concept_id_2': 'int64',
            'fact_id_2': 'int64',
            'relationship_concept_id': 'int64'
        }

        # Standardized health system data
        model_schema['location'] = {
            'location_id':  'int64',
            'address_1': 'category',
            'address_2': 'category',
            'city': 'category',
            'state': 'category',
            'zip': 'category',
            'county': 'category',
            'location_source_value': 'category'
        }

        model_schema['care_site'] = { 
            'care_site_id': 'int64',
            'care_site_name': 'category',
            'place_of_service_concept_id': 'int64',
            'location_id': 'int64',
            'care_site_source_value': 'category',
            'place_of_service_source_value': 'category'
        }

        model_schema['provider'] = {
            'provider_id': 'int64',
            'provider_name': 'category',
            'NPI': 'category',
            'DEA': 'category',
            'specialty_concept_id': 'int64',
            'care_site_id': 'int64',
            'year_of_birth': 'int64',
            'gender_concept_id': 'int64',
            'provider_source_value': 'category',
            'specialty_source_value': 'category',
            'specialty_source_concept_id': 'int64',
            'gender_source_value': 'category',
            'gender_source_concept_id': 'int64'  
        }

        # Standardized health economics
        model_schema['payer_plan_period'] = {
            'payer_plan_period_id': 'int64',
            'person_id': 'int64',
            'payer_plan_period_start_date': 'object',
            'payer_plan_period_end_date': 'object',
            'payer_concept_id': 'int64',
            'payer_source_value': 'category',
            'payer_source_concept_id': 'int64',
            'plan_concept_id': 'int64',
            'plan_source_value': 'category',
            'plan_source_concept_id': 'int64',
            'sponsor_concept_id': 'int64',
            'sponsor_source_value': 'category',
            'sponsor_source_concept_id': 'int64',
            'family_source_value': 'category',
            'stop_reason_concept_id': 'int64',
            'stop_reason_source_value': 'category',
            'stop_reason_source_concept_id': 'int64'       
        }

        model_schema['cost'] = {
            'cost_id': 'int64'  ,
            'cost_event_id': 'int64',
            'cost_domain_id': 'category',
            'cost_type_concept_id': 'int64',
            'currency_concept_id': 'int64',
            'total_charge': 'float',
            'total_cost': 'float',
            'total_paid': 'float',
            'paid_by_payer': 'float',
            'paid_by_patient': 'float',
            'paid_patient_copay': 'float',
            'paid_patient_coinsurance': 'float',
            'paid_patient_deductible': 'float',
            'paid_by_primary': 'float',
            'paid_ingredient_cost': 'float',
            'paid_dispensing_fee': 'float',
            'payer_plan_period_id': 'int64',
            'amount_allowed': 'float',
            'revenue_code_concept_id': 'int64',
            'reveue_code_source_value': 'category',
            'drg_concept_id': 'int64',
            'drg_source_value': 'category'
        }

        # Standardized derived elements
        model_schema['cohort'] = {
            'cohort_definition_id': 'int64',
            'subject_id': 'int64',
            'cohort_start_date:': 'object',
            'cohort_end_date:': 'object'
        }

        model_schema['cohort_attribute'] = {
            'cohort_definition_id': 'int64',
            'subject_id': 'int64',
            'cohort_start_date': 'object',
            'cohort_end_date': 'object',
            'attribute_definition_id': 'int64',
            'value_as_number': 'float',
            'value_as_concept_id': 'int64'
        }

        model_schema['drug_era'] = {
            'drug_era_id': 'int64',
            'person_id': 'int64',
            'drug_concept_id': 'int64',
            'drug_era_start_date': 'object',
            'drug_era_end_date': 'object',
            'drug_exposure_count': 'int64',
            'gap_days': 'int64'
        }

        model_schema['dose_era'] = {
            'dose_era_id': 'int64',
            'person_id': 'int64',
            'drug_concept_id': 'int64',
            'unit_concept_id': 'int64',
            'dose_value': 'float',
            'dose_era_start_date': 'object',
            'dose_era_end_date': 'object'  
        }

        model_schema['condition_era'] = {
            'condition_era_id': 'int64',
            'person_id': 'int64',
            'condition_concept_id': 'int64',
            'condition_era_start_date': 'object',
            'condition_era_end_date': 'object',
            'condition_occurrence_count': 'int64'
        }
        return model_schema
