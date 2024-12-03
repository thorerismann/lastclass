from repro_code.extra_charts import ExtraCharts
from repro_code.data_preparation import LoadReproData, SecondBlock
from repro_code.sumamry_stats_econ import print_summary_stats

def prepare_unemployment_regression():
    pass

def main():
    # ExtraCharts.plot_coal_jobs(Path.cwd() / 'data' / 'coal_jobs.csv')
    # ExtraCharts.plot_random_non_random()
    allcomp = LoadReproData.load_econometrics()
    allcomp_cc = LoadReproData.first_filter(allcomp)
    cc = LoadReproData.first_filter(allcomp_cc)
    # allcomp_cc_types = LoadReproData.second_filter(allcomp_cc, cc)
    print_summary_stats(allcomp, allcomp_cc)

    bea_fips_mods = LoadReproData.load_bea_fips_mods()
    print(bea_fips_mods.head())
    print(cc.head())

    xmat = SecondBlock.load_county_adj()
    print('got the xmat')
    xmat1 = SecondBlock.second_county_filter(xmat, bea_fips_mods)
    allcomp_full, xmat_fips = SecondBlock.third_county_filter(xmat1, allcomp)

    # weights = SecondBlock.fourth_county_filter(xmat_fips, xmat, filtered_econ)
    print('filtered the xmat')


main()
print('stop')