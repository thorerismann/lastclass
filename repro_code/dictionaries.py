
# sum_dict
sum_dict = {
    "Active Mines (no.)": None,
    "Unemployment Rate": None,
    "Employed Persons": None,
    "Unemployed Persons": None,
    "Labour Force": None,
    "Population": None,
    "Total USDA RE Investments in USD": None,
    "Coal Production (in short tons)": None,
    "Real GDP": None,
    "Real GDP Per Capita": None,
    "Rural-Urban Code": None,
    "Rural-Urban (binary)": None,
    "Total TAA Allocation in USD": None,
    "USDA RE Investments scaled by Real GDP": None
}

# sum_dict_trans
sum_dict_trans = {
    "Δ Unemployment Rate": None,
    "Δ Active Mines": None,
    "Δ (log) Real GDP": None,
    "Δ (log) Real GDP per capita": None,
    "Δ (log) Employed Persons": None,
    "Δ (log) Unemployed Persons": None,
    "Δ (log) Labour Force": None,
    "Δ (log) Population": None,
    "REE ≥ .1% of GDP": None
}

# cm
cm = {
    "lag_diff2": "Δ Active Mines (t-2)",
    "lag_diff": "Δ Active Mines (t-1)",
    "mines_diff": "Δ Active Mines"
}

# plot_dict
plot_dict = {
    "f(mines_diff,3)": "-3",
    "f(mines_diff,2)": "-2",
    "f(mines_diff, 1)": "-1",
    "mines_diff": "0",
    "lag_diff": "+1",
    "lag_diff2": "+2",
    "lag_diff3": "+3",
    "factor_type1:mines_diff": "0",
    "factor_type2:mines_diff": "0",
    "factor_type3:mines_diff": "0",
    "factor_type1:lag_diff": "+1",
    "factor_type2:lag_diff": "+1",
    "factor_type3:lag_diff": "+1",
    "factor_type1:lag_diff2": "+2",
    "factor_type2:lag_diff2": "+2",
    "factor_type3:lag_diff2": "+2",
    "factor_type1:f(mines_diff, 1)": "-1",
    "factor_type2:f(mines_diff, 1)": "-1",
    "factor_type3:f(mines_diff, 1)": "-1",
    "factor_type1:lag_diff3": "+3",
    "factor_type2:lag_diff3": "+3",
    "factor_type3:lag_diff3": "+3"
}

LA_list_missing = ["22051", "22071", "22075", "22087", "22089", "22095", "22103"]

setFixest_dict = {
    "emp": "Persons Employed in Coal",
    "employed": "Employed Persons",
    "uer": "Unemployment Rate",
    "active_mines": "Active Mines",
    "p_inc_1000": "County Personal Income (PI) in USD Millions",
    "p_inc_X": "County Personal Income (PI) in USD Billions",
    "pop_1000": "County Population (Thousands)",
    "fips": "County FIPS Code",
    "year": "Year",
    "lag_mines": "Active Mines (t-1)",
    "lag_mines2": "Active Mines (t-2)",
    "lag_mines3": "Active Mines (t-3)",
    "lag_mines4": "Active Mines (t-4)",
    "mines_diff": "Change Active Mines",
    "lag_diff": "Change Active Mines (t-1)",
    "lag_diff2": "Change Active Mines (t-2)",
    "lag_diff3": "Change Active Mines (t-3)",
    "diff_emp": "Change Persons Employed in Coal",
    "lag_diff_emp": "Change Persons Employed in Coal (t-1)",
    "lag_diff_emp2": "Change Persons Employed in Coal (t-2)",
    "diff_employed": "Change Employed Persons",
    "diff_uer": "Change Unemployment Rate",
    "green_emp": "Persons Employed in Green Sectors",
    "diff_green_emp": "Change Persons Employed in Green Sectors",
    "lag_emp": "Persons Employed in Coal (t-1)",
    "lag_emp2": "Persons Employed in Coal (t-2)",
    "ff_emp": "Persons Employed in FF (not incl. Coal)",
    "diff_ff_emp": "Change Persons Employed in FF (not incl. Coal)",
    "lag_diff_ffemp": "Change Persons Employed in FF (not incl. Coal) (t-1)",
    "lag_diff_ffemp2": "Change Persons Employed in FF (not incl. Coal) (t-2)",
    "diff_total_ff_emp": "Change Persons Employed in FF (incl. Coal)",
    "lag_diff_total_ffemp": "Change Persons Employed in FF (incl. Coal) (t-1)",
    "lag_diff_total_ffemp2": "Change Persons Employed in FF (incl. Coal) (t-2)",
    "type_factor1": "Type 1",
    "type_factor2": "Type 2",
    "type_factor3": "Type 3",
    "mine_closure": "Mine Closed (t)",
    "lag_closure": "Mine Closed (t-1)",
    "ruc_bin": "Rural",
    "REE_inv_scaled_pinc": "REE Investments (Proportion of County PI)",
    "logrealgdp_pc": "Real GDP per capita (log)",
    "diff_log_realgdp_pc": "Change in (log) Real GDPPC",
    "log_pop": "Population (log)",
    "log_realgdp": "Real GDP (log)",
    "diff_log_employed": "Change in Employed Persons (log)",
    "diff_log_unemployed": "Change in Unemployed Persons (log)",
    "diff_log_pop": "Change in Population (log)",
    "diff_log_lf": "Change in Labour Force (log)",
    "diff_log_realgdp": "Change in Real GDP (log)",
    "prod_diff": "Change in Production (short tons)",
    "lag_prod_diff": "Change in Production (short tons) (t-1)",
    "lag_prod_diff2": "Change in Production (short tons) (t-2)",
    "factor_type1": "Type 1",
    "factor_type2": "Type 2",
    "factor_type3": "Type 3",
    "f(mines_diff,1)": "Change Active Mines (t+1)",
    "emp_10": "NAICS 10 \n All industries",
    "emp_22": "NAICS 22 \n Utilities",
    "emp_23": "NAICS 23 \n Construction",
    "emp_42": "NAICS 42 \n Wholesale trade",
    "emp_51": "NAICS 51 \n Information",
    "emp_52": "NAICS 52 \n Finance and \n insurance",
    "emp_53": "NAICS 53 \n Real estate and \n rental and leasing",
    "emp_54": "NAICS 54 \n Professional, scientific, \n and technical services",
    "emp_71": "NAICS 71 \n Arts, entertainment, \n and recreation",
    "emp_72": "NAICS 72 \n Accommodation \n and food services",
    "emp_81": "NAICS 81 \n Other services \n (except public administration)",
    "emp_92": "NAICS 92 \n Public administration",
    "emp_11": "NAICS 11 \n Agriculture, forestry, \n fishing and hunting",
    "emp_21": "NAICS 21 \n Mining, quarrying, and \n oil and gas extraction",
    "emp_55": "NAICS 55 \n Management of companies \n and enterprises",
    "emp_56": "NAICS 56 \n Administrative and \n support and waste management \n and remediation services",
    "emp_61": "NAICS 61 \n Educational \n services",
    "emp_62": "NAICS 62 \n Health care and \n social assistance",
    "diff_log_emp_10": "NAICS 10 \n All industries",
    "diff_log_emp_22": "NAICS 22 \n Utilities",
    "diff_log_emp_23": "NAICS 23 \n Construction",
    "diff_log_emp_42": "NAICS 42 \n Wholesale trade",
    # Add the remaining key-value pairs here
}


def dict_return(key):
    """Returns the desired dictionary"""
    dicts = {
        'LA_list_missing': LA_list_missing,
        'plot_dict': plot_dict,
        'cm': cm,
        'sum_dict_trans': sum_dict_trans,
        'sum_dict': sum_dict,
        'setFixest_dict': setFixest_dict
    }
    return dicts[key]