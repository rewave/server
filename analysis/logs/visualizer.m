%visualize data logs

ls 
log_file = input('Enter file to visualize : ', 's');

data = load(log_file);

t  = data(:,1);
ax = data(:,2);
ay = data(:,3);
az = data(:,4);
wx = data(:,5);
wy = data(:,6);
wz = data(:,7);
