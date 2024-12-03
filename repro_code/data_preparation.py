import numpy as np
import pandas as pd
from pathlib import Path
# from pysal.lib import weights

class LoadReproData:
    @staticmethod
    def load_econometrics():
        print('loading econometrics file')
        # Use pandas to read the Excel file
        df = pd.read_excel(Path.cwd() / 'data' / 'Econometrics_Final.xlsx')
        return df

    @staticmethod
    def load_bea_fips_mods():
        print('loading bea fips mods file')
        # Use pandas to read the Excel file
        df = pd.read_excel(Path.cwd() / 'data' / 'FIPSModificationsVA.xlsx', skiprows=1, dtype=str)
        return df

    @staticmethod
    def carbon_clusters():
        print('loading carbon clusters file')
        df = pd.read_excel(Path.cwd() / 'data' / 'cc_clusters_251.xlsx', dtype=str)
        return df

    @staticmethod
    def first_filter(allcomp):
        print('first data filter')
        cclist = allcomp.loc[allcomp["active_mines"] != 0, "fips"].unique()
        allcomp_cc = allcomp[allcomp["fips"].isin(cclist)]
        return allcomp_cc

    @staticmethod
    def second_filter(allcomp_cc, cc_cluster ):
        # Perform the merge in pandas
        allcomp_cc_types = pd.merge(allcomp_cc, cc_cluster, on="fips", how="left")

        # Display the result
        return allcomp_cc_types




class SecondBlock:
    @staticmethod
    def load_county_adj():
        "columns 137 to 147"
        print('loading county adj file')
        xmat1 = pd.read_table(
            Path.cwd() / "data" / "county_adjacency.txt",
            sep="\t",
            header=None,
            dtype=str,  # Ensures all columns are strings
            names=["V1", "V2", "V3", "V4"]  # Name the columns for clarity
        )

        # Retain only the columns with FIPS codes
        xmat1 = xmat1[["V2", "V4"]]

        # Fill missing values in V2 with the last valid observation (forward fill)
        xmat1["V2"] = xmat1["V2"].fillna(method="ffill")

        # Define a function to format FIPS codes
        def fips_format(fipscode):
            if pd.isna(fipscode):  # Handle missing values
                return "00000"
            fipscode = str(fipscode)
            return fipscode.zfill(5)  # Ensure 5 characters with leading zeros if needed

        # Apply formatting to both columns
        xmat1["V2"] = xmat1["V2"].apply(fips_format)
        xmat1["V4"] = xmat1["V4"].apply(fips_format)
        return xmat1

    @staticmethod
    def second_county_filter(xmat1, bea_fips_mods):
        """Aligns with lines 149 - 168"""

        getfips = pd.Series(bea_fips_mods["BEA FIPS"].values, index=bea_fips_mods["FIPS"]).to_dict()

        # Replace specific FIPS codes
        xmat1["V2"] = xmat1["V2"].replace({"46113": "46102", "51515": "51019"})
        xmat1["V4"] = xmat1["V4"].replace({"46113": "46102", "51515": "51019"})

        # Step 2: Map `V2` and `V4` using the lookup table
        xmat1["V2"] = xmat1["V2"].apply(lambda x: getfips[x] if x in getfips else x)
        xmat1["V4"] = xmat1["V4"].apply(lambda x: getfips[x] if x in getfips else x)

        # Step 3: Remove Alaska, Hawaii, DC, PR, Guam, American Samoa
        xmat1 = xmat1[~xmat1["V2"].str.startswith(("60", "66", "69", "72", "78", "15", "02"))].copy()

        # Step 4: Remove rows with specified `LA_list` entries in `V2` or `V4`
        LA_list_missing = ["22051", "22071", "22075", "22087", "22089", "22095", "22103"]
        LA_list = LA_list_missing + ["11001"]
        getfips = pd.Series(bea_fips_mods["BEA FIPS"].values, index=bea_fips_mods["FIPS"]).to_dict()

        # Replace specific FIPS codes
        xmat1["V2"] = xmat1["V2"].replace({"46113": "46102", "51515": "51019"})
        xmat1["V4"] = xmat1["V4"].replace({"46113": "46102", "51515": "51019"})

        # Step 2: Map `V2` and `V4` using the lookup table
        xmat1["V2"] = xmat1["V2"].apply(lambda x: getfips[x] if x in getfips else x)
        xmat1["V4"] = xmat1["V4"].apply(lambda x: getfips[x] if x in getfips else x)

        xmat1 = xmat1[~xmat1["V2"].isin(LA_list) & ~xmat1["V4"].isin(LA_list)]
        return xmat1

    @staticmethod
    def third_county_filter(xmat1, allcomp):
        """Lines 169 - 184"""
        # Step 1: Create a list of unique FIPS codes for matching
        fipslist = xmat1["V2"].unique()

        # Step 2: Subset `allcomp` to only include FIPS present in the distance matrix
        allcomp_nomissing = allcomp[allcomp["fips"].isin(fipslist)]

        # Optional: Exclude specific FIPS codes (uncomment if needed)
        # allcomp_nomissing = allcomp_nomissing[allcomp_nomissing["fips"] != "51770"]

        # Step 3: Arrange `allcomp_nomissing` by FIPS and rearrange columns
        allcomp_full = allcomp_nomissing.sort_values(by="fips").reset_index(drop=True)

        # If "year" column exists, move it next to "fips"
        if "year" in allcomp_full.columns:
            cols = ["fips", "year"] + [col for col in allcomp_full.columns if col not in ["fips", "year"]]
            allcomp_full = allcomp_full[cols]

        # Step 4: Extract unique FIPS codes from `xmat1`
        xmatfips = xmat1["V2"].unique()
        return allcomp_full, xmatfips

    @staticmethod
    def fourth_county_filter(xmatfips, xmat1, allcomps):
        """Lines 187 - 204"""
        n = len(xmatfips)
        fmat = np.zeros((n, n), dtype=float)
        fips_index = {fips: idx for idx, fips in enumerate(xmatfips)}  # Map FIPS to index for quick lookup

        # Step 2: Populate the distance matrix
        for _, row in xmat1.iterrows():
            a = row["V2"]
            b = row["V4"]
            if a != b:  # Counties are neighbors
                fmat[fips_index[a], fips_index[b]] = 1

        # Step 3: Row-standardize the distance matrix
        row_sums = fmat.sum(axis=1)
        fmat = np.divide(fmat, row_sums[:, np.newaxis], where=row_sums[:, np.newaxis] != 0)

        # Step 4: Check for NA values and matrix dimensions
        print(f"Number of NA values: {np.isnan(fmat).sum()}")
        print(f"Matrix dimensions: {fmat.shape}")

        # Step 5: Create a weights object for spatial analysis
        w = weights.W(fmat, id_order=xmatfips)
        return w




