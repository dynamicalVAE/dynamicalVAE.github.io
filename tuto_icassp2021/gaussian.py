# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(0)

plt.close('all')

training_samples = np.random.randn(100)


mu_est = np.mean(training_samples)
sigma_est = np.std(training_samples)

print(mu_est)
print(sigma_est)


fig, ax = plt.subplots(1, 1)
x = np.linspace(-4, 4, 1000)

ax.plot(x, norm.pdf(x, 0, 1), color='tab:blue', linestyle='-.', lw=2, alpha=1, label='true distribution')


ax.plot(x, norm.pdf(x, mu_est, sigma_est), color='tab:orange', linestyle='--', lw=2, alpha=1, label='model distribution')



test_samples = mu_est + sigma_est*np.random.randn(100)

ax.plot(training_samples, np.zeros_like(training_samples), 'x', label='training samples')
ax.plot(test_samples, -0.01*np.ones_like(test_samples), '+', label='generated samples')

plt.xlabel('x', fontsize=15)

plt.ylabel('p(x)', fontsize=15)


handles, labels = ax.get_legend_handles_labels()
# sort both labels and handles by labels
labels, handles = zip(*sorted(zip(labels, handles), key=lambda t: t[0]))
ax.legend(handles[::-1], labels[::-1], fontsize=14)

plt.tight_layout()
