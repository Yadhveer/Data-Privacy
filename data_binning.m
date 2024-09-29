% Sample Data
data = [
    25, 55000, 12;  % Low Age, Medium Income, High Purchases
    35, 42000, 13;  % Medium Age, Low Income, High Purchases
    48, 72000, 6;   % High Age, Medium Income, Low Purchases
    22, 78000, 8;   % Low Age, High Income, Medium Purchases
    34, 65000, 4;   % Medium Age, Medium Income, Low Purchases
    45, 39000, 7;   % High Age, Low Income, Medium Purchases
    26, 58000, 15;  % Low Age, Medium Income, High Purchases
    32, 70000, 5;   % Medium Age, High Income, Low Purchases
    50, 44000, 9;   % High Age, Low Income, Medium Purchases
    28, 52000, 14;  % Low Age, Medium Income, High Purchases
    31, 73000, 4;   % Medium Age, High Income, Low Purchases
    47, 39000, 11;  % High Age, Low Income, Medium Purchases
    23, 60000, 16;  % Low Age, Medium Income, High Purchases
    30, 72000, 4;   % Medium Age, High Income, Low Purchases
    49, 46000, 10;  % High Age, Low Income, Medium Purchases
    24, 55000, 18;  % Low Age, Medium Income, High Purchases
    36, 68000, 5;   % Medium Age, High Income, Low Purchases
    44, 47000, 12;  % High Age, Low Income, Medium Purchases
    27, 59000, 17;  % Low Age, Medium Income, High Purchases
    33, 71000, 10;  % Medium Age, High Income, Low Purchases
    42, 48000, 8;   % High Age, Low Income, Medium Purchases
    25, 56000, 14;  % Low Age, Medium Income, High Purchases
    38, 70000, 3;   % Medium Age, High Income, Low Purchases
    46, 42000, 9;   % High Age, Low Income, Medium Purchases
    29, 55000, 15;  % Low Age, Medium Income, High Purchases
    37, 69000, 5;   % Medium Age, High Income, Low Purchases
    45, 48000, 10;  % High Age, Low Income, Medium Purchases
    21, 53000, 17;  % Low Age, Medium Income, High Purchases
    39, 65000, 4;   % Medium Age, High Income, Low Purchases
    49, 49000, 11;  % High Age, Low Income, Medium Purchases
    29, 55000, 15;  % Low Age, Medium Income, High Purchases
];

% Initialize Binned Data
binnedData = strings(size(data, 1), 3);  % Use string array for simpler handling

% Binning criteria for Age, Income, and Purchases
for i = 1:size(data, 1)
    % Binning Age
    if data(i, 1) >= 20 && data(i, 1) <= 30
        binnedData(i, 1) = "low";
    elseif data(i, 1) >= 31 && data(i, 1) <= 40
        binnedData(i, 1) = "medium";
    elseif data(i, 1) >= 41 && data(i, 1) <= 60
        binnedData(i, 1) = "high";
    else
        binnedData(i, 1) = "unknown";
    end
    
    % Binning Income
    if data(i, 2) < 50000
        binnedData(i, 2) = "low";
    elseif data(i, 2) >= 50000 && data(i, 2) < 70000
        binnedData(i, 2) = "medium";
    else
        binnedData(i, 2) = "high";
    end
    
    % Binning Purchases
    if data(i, 3) < 5
        binnedData(i, 3) = "low";
    elseif data(i, 3) >= 5 && data(i, 3) < 10
        binnedData(i, 3) = "medium";
    else
        binnedData(i, 3) = "high";
    end
end

% Define labels for each attribute
attributeLabels = {"Age", "Income", "Purchases"};

disp(binnedData)
