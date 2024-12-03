"""This module prints the statistics tables in the supplementary materials section of the appendix, tables S2 - S5."""

def print_summary_stats(allcomp, allcomp_cc):
    """Function to print the 3rd markdown section summary statistics reported by the authors."""
    # Summary statistics for the first DataFrame (allcomp)
    summary_allcomp = allcomp[[
        "active_mines", "uer", "employed", "unemployed",
        "labour_force", "pop", "REE_inv",
        "realgdp", "realgdp_pc", "ruc", "ruc_bin",
        "REE_inv_scaled_realgdp"
    ]].describe()

    print("Summary Statistics: Contiguous US Counties")
    print(summary_allcomp)

    # Summary statistics for the second DataFrame (allcomp_cc)
    summary_allcomp_cc = allcomp_cc[[
        "active_mines", "uer", "employed", "unemployed",
        "labour_force", "pop", "REE_inv",
        "realgdp", "realgdp_pc", "ruc", "ruc_bin",
        "REE_inv_scaled_realgdp"
    ]].describe()

    print("\nSummary Statistics: US Coal Counties")
    print(summary_allcomp_cc)

    # Summary statistics for transformed variables (allcomp)
    summary_trans_allcomp = allcomp[[
        "diff_uer", "mines_diff", "diff_log_realgdp",
        "diff_log_realgdp_pc", "diff_log_employed",
        "diff_log_unemployed", "diff_log_lf", "diff_log_pop",
        "REE_bin_top90"
    ]].describe()

    print("\nSummary Statistics of Transformed Variables: Contiguous US Counties")
    print(summary_trans_allcomp)

    # Summary statistics for transformed variables (allcomp_cc)
    summary_trans_allcomp_cc = allcomp_cc[[
        "diff_uer", "mines_diff", "diff_log_realgdp",
        "diff_log_realgdp_pc", "diff_log_employed",
        "diff_log_unemployed", "diff_log_lf", "diff_log_pop",
        "REE_bin_top90"
    ]].describe()

    print("\nSummary Statistics of Transformed Variables: US Coal Counties Subset")
    print(summary_trans_allcomp_cc)
