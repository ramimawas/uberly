
%% Initialization
clear ; close all; clc

%{
m = 484;	% training size
fileX = 'tweetsX.txt';
fileY = 'tweetsY.txt';
modelName = 'model.012.mat';
%}

m = 434;	% training size
fileX = 'tweetsX.tmp.12.txt';
fileY = 'tweetsY.tmp.12.txt';
modelName = 'model.12.mat';

n = 966;	% feature size
fileVocab = 'uber_vocab.txt';

% Load X
fid = fopen(fileX);
x = cell(m, 1);
i=1;
fprintf('\nLoading X...');
while((line=fgetl(fid)) != -1)
    fprintf('.'); if exist('OCTAVE_VERSION') fflush(stdout); end
	x{i++} = line;
end
fprintf(' %d', m);
fclose(fid);

% Load Y
fprintf('\nLoading Y... %d', m);
y = load(fileY);

% Load Vocabulary
fprintf('\nLoading vocabulary... %d\n', n);
vocabList = loadVocab(fileVocab, n);

% Load features
fprintf('\nLoading features');
X = zeros(m, n);
for i = 1:m
	word_indices  = extractFeatures(x{i}, vocabList);
	X(i,:) = mapFeatures(word_indices, n)';
    fprintf('.'); if exist('OCTAVE_VERSION') fflush(stdout); end
end
fprintf(' %d', m);
fprintf('\nProgram paused. Press enter to continue.\n');pause;

%train
C = 0.3;
model = svmTrain(X, y, C, @linearKernel);
fprintf('\nSaving model... %s', modelName);
save('-binary', modelName, 'model');

fprintf('\nProgram paused. Press enter to continue.\n');pause;

% Sort the weights and obtin the vocabulary list
[weight, idx] = sort(model.w, 'descend');
fprintf('\nTop predictors of positive: \n');
for i = 1:15
    fprintf(' %-15s (%f) \n', vocabList{idx(i)}, weight(i));
end

fprintf('\nProgram paused. Press enter to continue.\n');pause;

tweet = "@BeingNOLA #Uber is a great service. I've used the service in multiple cities. Way more efficient than any service we currently have.";
p = svmPredict(model, mapFeatures(extractFeatures(tweet, vocabList), n));
fprintf('\nProcessed %s\n\nUberly Classification: %d\n', tweet, p);
fprintf('(1 indicates positive, 0 indicates neutral/negative)\n\n');

% Testing
fprintf('\nEvaluating the trained Linear SVM on a test set ...\n')
p = svmPredict(model, X);
fprintf('Training Accuracy: %f\n', mean(double(p == y)) * 100);

