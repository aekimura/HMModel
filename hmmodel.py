#!/usr/bin/env python

import numpy as np
from hmmlearn import hmm
import math

states = {'Rainy', 'Sunny'}
observations = {'happy', 'sad'}
start_probability = {'Rainy': 0.3333333333, 'Sunny': 0.6666666667}
transition_probability = {
	'Rainy': {'Rainy': 0.6, 'Sunny': 0.4},
	'Sunny': {'Rainy': 0.2, 'Sunny': 0.8}}
emission_probability = {
	'Rainy': {'happy': 0.4, 'sad': 0.6},
	'Sunny': {'happy': 0.8, 'sad': 0.2}}

model = hmm.MultinomialHMM(n_components=2)
model.startprob_ = np.array([0.3333333333, 0.6666666667])
model.transmat_ = np.array([[0.6, 0.4],[0.2, 0.8]])
model.emissionprob_ = np.array([[0.4, 0.6],[0.8, 0.2]])

def print_states(seq):
	'''Returns a string of the most likely state pattern'''
	st = ['Rainy', 'Sunny']
	result = 'Most Likely State Pattern: '
	for s in seq:
		result = result + st[s] + ' -> '
	print(result[:-4])

if __name__ == '__main__':
	print('Hidden Markov Model Homework')
	print(' ')
	print('2-day:\n  day 1 = happy\n  day 2 = sad')
	logprob, seq = model.decode(np.array([[0, 1]]).transpose())
	print_states(seq)
	print('Probability: \t' + str(math.exp(logprob)))
	print(' ')

	print('3-day:\n  day 1 = happy\n  day 2 = sad\n  day 3 = happy')
	logprob, seq = model.decode(np.array([[0, 1, 0]]).transpose())
	print_states(seq)
	print('Probability: \t' + str(math.exp(logprob)))
	print(' ')

	print('6-day:\n  day 1 = happy\n  day 2 = happy\n  day 3 = sad' +\
		'\n  day 4 = sad\n  day 5 = sad\n  day 6 = happy')
	logprob, seq = model.decode(np.array([[0, 0, 1, 1, 1, 0]]).transpose())
	print_states(seq)
	print('Probability: \t' + str(math.exp(logprob)))
	print(' ')

	print('7-day:\n  day 1 = happy\n  day 2 = sad\n  day 3 = happy\n' +\
                '  day 4 = sad\n  day 5 = happy\n  day 6 = sad\n  day 7 = happy')
        logprob, seq = model.decode(np.array([[0, 1, 0, 1, 0, 1, 0]]).transpose())
        print_states(seq)
        print('Probability: \t' + str(math.exp(logprob)))
        print(' ')
