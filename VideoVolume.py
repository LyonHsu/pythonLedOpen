import alsaaudio

m=alsaaudio.Mixer();
vol=m.getvolume();
print('vol = %d',vol);
vol=int(vol[0]);
print('vol int=%d',vol);

newvol =  vol+10;  #set vol +10 range(0~100)
m.setvolume(newvol);

print('set vol = %d',m.getvolume());
