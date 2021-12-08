row[5] = sum
if (row[5] == 3.25 and row[0] >= quantile_75[0] and row[2] >= quantile_75[2]) or \
        (row[5] == 3.25 and row[0] < quantile_50[0] and row[2] < quantile_50[2]) or \
        (row[5] == 3.25 and quantile_50[0] <= row[0] < quantile_75[0] and quantile_50[2] <= row[2] <
         quantile_75[2]):
    row[5] += 1.75
elif (row[5] == 3.25 and quantile_50[0] <= row[0] < quantile_75[0] and row[2] >= quantile_75[2]) or \
        (row[5] == 3.25 and quantile_50[2] <= row[2] < quantile_75[2] and row[0] >= quantile_75[0]):
    row[5] += 1.5
elif (row[5] == 3.25 and quantile_50[0] <= row[0] < quantile_75[0] and row[2] < quantile_50[2]) or \
        (row[5] == 3.25 and quantile_50[2] <= row[2] < quantile_75[2] and row[0] < quantile_50[0]):
    row[5] += 1.25
elif (row[5] == 3.25 and row[0] >= quantile_75[0] and row[2] < quantile_50[2]) or \
        (row[5] == 3.25 and row[2] >= quantile_75[2] and row[0] < quantile_50[0]):
    row[5] += 1

elif (row[5] == 3.0 and row[0] >= quantile_75[0] and row[2] >= quantile_75[2]) or \
        (row[5] == 3.0 and row[0] < quantile_50[0] and row[2] < quantile_50[2]) or \
        (row[5] == 3.0 and quantile_50[0] <= row[0] < quantile_75[0] and quantile_50[2] <= row[2] <
         quantile_75[
             2]):
    row[5] += 1.75
elif (row[5] == 3.0 and quantile_50[0] <= row[0] < quantile_75[0] and row[2] >= quantile_75[2]) or \
        (row[5] == 3.0 and quantile_50[2] <= row[2] < quantile_75[2] and row[0] >= quantile_75[0]):
    row[5] += 1.5
elif (row[5] == 3.0 and quantile_50[0] <= row[0] < quantile_75[0] and row[2] < quantile_50[2]) or \
        (row[5] == 3.0 and quantile_50[2] <= row[2] < quantile_75[2] and row[0] < quantile_50[0]):
    row[5] += 1.25
elif (row[5] == 3.0 and row[0] >= quantile_75[0] and row[2] < quantile_50[2]) or \
        (row[5] == 3.0 and row[2] >= quantile_75[2] and row[0] < quantile_50[0]):
    row[5] += 1