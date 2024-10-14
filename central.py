import numpy as np
import matplotlib.pyplot as plt

def simulate_central_limit(n_samples, n_trials, distribution='uniform', params=None):
    """
    Simule le Théorème Central Limite.
    
    :param n_samples: Nombre d'échantillons par essai.
    :param n_trials: Nombre d'essais.
    :param distribution: Type de distribution ('uniform', 'normal', 'exponential').
    :param params: Paramètres de la distribution, si nécessaire.
    :return: Les moyennes des échantillons.
    """
    
    means = []
    
    for _ in range(n_trials):
        if distribution == 'uniform':
            data = np.random.uniform(params[0], params[1], n_samples)
        elif distribution == 'normal':
            data = np.random.normal(params[0], params[1], n_samples)
        elif distribution == 'exponential':
            data = np.random.exponential(params[0], n_samples)
        else:
            raise ValueError("Distribution non reconnue.")
        
        means.append(np.mean(data))
    
    return means

def plot_results(means):
    """
    Affiche l'histogramme des moyennes et la distribution normale théorique.
    
    :param means: Liste des moyennes des échantillons.
    """
    plt.figure(figsize=(10, 6))
    plt.hist(means, bins=30, density=True, alpha=0.6, color='g')
    
    # Calcul de la moyenne et de l'écart type
    mu = np.mean(means)
    sigma = np.std(means)
    
    # Création des valeurs pour la courbe normale
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
    plt.plot(x, (1/(sigma * np.sqrt(2 * np.pi))) * np.exp(- (x - mu)**2 / (2 * sigma**2)), 
             color='r', lw=2)
    
    plt.title('Théorème Central Limite')
    plt.xlabel('Moyennes')
    plt.ylabel('Densité')
    plt.grid()
    plt.show()