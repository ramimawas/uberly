function word_indices = extractFeatures(tweet, vocabList)

word_indices = [];
%fprintf('\nraw: %s\n', tweet);

% Preprocess Tweet

% Lower case
tweet = lower(tweet);

% Strip all HTML
% Looks for any expression that starts with < and ends with > and replace
% and does not have any < or > in the tag it with a space
tweet = regexprep(tweet, '<[^<>]+>', ' ');

% Handle Numbers
% Look for one or more characters between 0-9
tweet = regexprep(tweet, '[0-9]+', 'number');

% Handle URLS
% Look for strings starting with http:// or https://
tweet = regexprep(tweet, ...
                           '(http|https)://[^\s]*', 'httpaddr');

% Handle Email Addresses
% Look for strings with @ in the middle
tweet = regexprep(tweet, '[^\s]+@[^\s]+', 'emailaddr');

% Handle $ sign
tweet = regexprep(tweet, '[$]+', 'dollar');

%fprintf('\nnormalized tweet: %s\n', tweet);

% Process file
l = 0;

ftweet = '';
% Tokenize Tweet
while ~isempty(tweet)
    % Tokenize and also get rid of any punctuation
    [str, tweet] = ...
       strtok(tweet, ...
              [' @$/#.-:&*+=[]?!(){},''">_<;%' char(10) char(13)]);
   
    % Remove any non alphanumeric characters
    str = regexprep(str, '[^a-zA-Z0-9]', '');
    %fprintf('\nclean string: %s\n', str);

    % Stem the word 
    % (the porterStemmer sometimes has issues, so we use a try catch block)
    try str = porterStemmer(strtrim(str));
    catch str = ''; continue;
    end;

    % Skip the word if it is too short
    if length(str) < 1
       continue;
    end
    
	m = ismember(vocabList, str);
	if(length(m)>0)
		word_indices = [word_indices; find(m)];
	end

    % =============================================================


    % Print to screen, ensuring that the output lines are not too long
    if (l + length(str) + 1) > 78
        l = 0;
    end
	%fprintf('final string: %s\n', str);
	
	if (length(ftweet)>0)
		ftweet = strcat(ftweet, ',');
	end
	ftweet = strcat(ftweet, str);
    l = l + length(str) + 1;
end

%fprintf('final: %s\n', ftweet);
%fprintf('word_indices: %s\n', mat2str(word_indices'));
%fprintf('\n\n=========================\n');

end
