import utils
import sys
import os
import interpolation


def main(inp):
    data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/USD rates.csv'))
    rates = utils.extract_rates(data_path)

    def dates_to_diff(inp_dates):
        res = map(lambda date: (date - rates.index[0]).days, inp_dates)
        return list(res)

    dates = utils.parse_dates(inp)
    diff = dates_to_diff(dates)

    # data for interpolator
    xs = dates_to_diff(rates.index)
    ys = rates.values
    interpolator = interpolation.LinearInterpolator(xs=xs, ys=ys)

    rates = interpolator.interpolate_array(diff)
    return list(zip(inp, rates))


if __name__ == "__main__":
    args = input().split()
else:
    args = sys.argv[1:]

print(main(args))