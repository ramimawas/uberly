
%% Initialization
clear ; close all; clc

modelName = 'model.12.mat';
n = 966;	% feature size
fileVocab = 'uber_vocab.txt';

% Load Model
%fprintf('\nLoading model... %s', modelName);
load(modelName);

% Load Vocabulary
%fprintf('\nLoading vocabulary... %d', n);
vocabList = loadVocab(fileVocab, n);

args = argv();
tweet = args{1};

p = svmPredict(model, mapFeatures(extractFeatures(tweet, vocabList), n));
%fprintf('\nProcessed %s\n\nUberly Classification: %d\n', tweet, p);
%fprintf('(1 indicates positive, 0 indicates neutral/negative)\n\n');
fprintf('%d', p);

