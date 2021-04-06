import numpy
import matplotlib.pyplot as pyplot
from scipy.stats import binom
from matplotlib.lines import Line2D
import copy

prob_pearls = 20.0 / 423.0
num_prob_pearl_boost = 41
prob_pearl_boost_arr = numpy.linspace(1, 5, num_prob_pearl_boost)
num_monte_carlo = 1000000
num_pearls_needed = 10

gold_needed_arr = numpy.zeros([num_monte_carlo, num_prob_pearl_boost])

trades_needed_arr = numpy.zeros([num_monte_carlo, num_prob_pearl_boost])

for iboost in range(num_prob_pearl_boost):
    for imc in range(num_monte_carlo):
        current_pearls = 0
        current_gold = 0
        current_trades = 0

        while current_pearls < num_pearls_needed:
            current_gold = current_gold + 1
            if numpy.random.uniform() < prob_pearls * prob_pearl_boost_arr[iboost]:
                current_trades = current_trades + 1
                current_pearls = current_pearls + numpy.round(4 * numpy.random.uniform() + 0.5) + 3
        gold_needed_arr[imc, iboost] = current_gold
        trades_needed_arr[imc, iboost] = current_trades

max_gold = 500
prob_this_gold_arr = numpy.zeros([max_gold, num_prob_pearl_boost])
for igrid in range(num_prob_pearl_boost):
    for this_gold in range(max_gold):
        prob_this_gold_arr[this_gold, igrid] = numpy.sum(gold_needed_arr[:, igrid] == this_gold) / num_monte_carlo

dream_trades = [22, 5, 24, 18, 4, 1, 7, 12, 26, 8, 5, 20, 2, 13, 10, 10, 21, 20, 10, 3, 18, 3, 27, 4, 13, 5, 35, 70, 11,
                7, 24, 34, 7, 15, 10, 1, 40, 50, 5]

dream_successes = [3, 2, 2, 2, 0, 1, 2, 5, 3, 2, 2, 2, 0, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 0, 0, 1, 1, 2, 0, 1, 0, 0, 0, 0,
                   0, 0, 3, 2, 0]

dream_goalof12 = [1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 1, 0, 0]

dream_goalof10 = [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 11, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 1, 1, 0]

this_trade_prob = numpy.zeros([len(dream_trades), num_prob_pearl_boost])

for iboost in range(num_prob_pearl_boost):
    for this_trade in range(len(dream_trades)):
        if dream_goalof12[this_trade] == 1:
            this_trade_prob[this_trade, iboost] = prob_this_gold_arr[dream_trades[this_trade], iboost]

        else:
            if dream_trades[this_trade] == dream_successes[this_trade]:
                this_trade_prob[this_trade, iboost] = (prob_pearls * prob_pearl_boost_arr[iboost]) ** (
                dream_successes[this_trade])

            else:
                this_trade_prob[this_trade, iboost] = binom.pmf(dream_successes[this_trade], dream_trades[this_trade],
                                                                prob_pearls * prob_pearl_boost_arr[iboost])

ignore_last_barter = True

if ignore_last_barter:
    last_barter_correction = -1
else:
    last_barter_correction = 0

total_prob = numpy.product(this_trade_prob[0:len(this_trade_prob) + last_barter_correction, :], axis=0)

print(total_prob / numpy.sum(total_prob))
