# FOOD-LABELING-SYSTEM

### Librerie utilizzate
- ```sklearn``` per la costruzione del classificatore knn, del random forest per il task di classificazione, k-means per l'individuazione degli elementi simili;
- ```pgmpy```  per creare una rete bayesiana per il calcolo probabilistico sulla bontà in termini nutrizionali dell'alimento; 
- ```pandas``` per l'estrazione di dati contenuti in un dataset;

### Funzionamento
- a partire da valori nutrizionali, quali ```kCalorie```, ```proteine```, ```grassi``` e ```carboidrati``` su 100g, contenuti in un alimento, predice:
  - il Nutriscore [A-E] (mediante ```classificatore```)
  - se l'alimento é prevalentemente sano/nocivo (mediante ```Rete Bayesiana```)
  - gli alimenti con valori nutrizionali simili (mediante ```hard clustering```)

### Struttura
- il progetto si suddivide in più moduli disponibili nella directory ```food```, di seguito elencati:
  1. ```main.py``` avvia il programma, permettendo l'inserimento dei dati e successiva predizione;
  2. ```nutriscore_classification.py``` contiene i modelli knn e random forest utilizzati per il task di ```classificazione```;
  3. ```bayesian_network.py``` contiene la rete bayesiana ed il relativo ```modello probabilistico```;
  4. ```clustering.py``` contiene il modello kMeans utilizzato per il ```clustering``` del dataset;
  5. ```hyperparameter_optimization.py``` contiene la logica dietro all'```ottimizzazione dei parametri``` per i modelli knn e random forest;
  6. ```cross_validation.py``` contiene l'implementazione della ```k-fold cross-validation``` per la valutazione delle prestazioni dei modelli supervisionati;
  7. ```read_csv.py``` contiene il metodo per ```l'estrazione di dati``` da un dataset;
  8. ```test.py``` permette il ```testing``` dei modelli supervisionati, con relativa ottimizzazione di iperparametri e cross-validation.
- il dataset utilizzato si trova all'interno della directory ```data``` in formato ```.csv```;
