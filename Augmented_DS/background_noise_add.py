import scaper
import numpy as np
import os
import librosa

# OUTPUT FOLDER
outfolder_SNR30 = './scapes_SNR30'
outfolder_SNR15 = './scapes_SNR15'
outfolder_SNR0 = './scapes_SNR0'
outfolder_SNRneg15 = './scapes_SNR-15'
out_array=[outfolder_SNR30, outfolder_SNR15, outfolder_SNR0, outfolder_SNRneg15]


# SCAPER SETTINGS
fg_folder = './foreground'
bg_folder = './background'

n_soundscapes_gun = 20000
n_soundscapes_other = 20000
ref_db = -50
duration = 2.0 

min_events = 1
max_events = 1

event_time_dist = 'const'
#event_time_mean = 2.0
#event_time_std = 2.0
#event_time_min = 2.0
#event_time_max = 2.0
event_time = 0.0

source_time_dist = 'const'
source_time = 0.0

event_duration_dist = 'const'
#event_duration_min = 2.0
#event_duration_max = 2.0
event_duration = 2.0

snr_dist = 'const'
snr = 30
# snr_max = 30

pitch_dist = 'uniform'
pitch_min = -3.0
pitch_max = 3.0

time_stretch_dist = 'uniform'
time_stretch_min = 1
time_stretch_max = 1
    
# Generate 1000 soundscapes using a truncated normal distribution of start times
for m in range(4):
    outfolder=out_array[m]
    print(outfolder)
    for n in range(n_soundscapes_gun):
        
        if (n%1000==0):
            print('Generating soundscape with gunshot: {:d}/{:d}'.format(n+1, n_soundscapes_gun))

        # create a scaper
        sc = scaper.Scaper(duration, fg_folder, bg_folder)
        sc.protected_labels = []
        sc.ref_db = ref_db

        # add background
        sc.add_background(label=('choose', []), 
                          source_file=('choose', []), 
                          source_time=('const', 0))

        # add random number of foreground events
        #n_events = np.random.randint(min_events, max_events+1)
        #for _ in range(n_events):
        sc.add_event(label=('const','gun_shot'), 
                        source_file=('choose', []), 
                        source_time=(source_time_dist, source_time), 
                        event_time=(event_time_dist, event_time), 
                        event_duration=(event_duration_dist, event_duration), 
                        snr=(snr_dist, snr),
                        pitch_shift=(pitch_dist, pitch_min, pitch_max),
                        time_stretch=None)

        # generate
        audiofile = os.path.join(outfolder, "gun_shot.Soundscape_{:d}.wav".format(n))
        jamsfile = os.path.join(outfolder, "gun_shot.Soundscape_{:d}.jams".format(n))
        txtfile = os.path.join(outfolder, "gun_shot.Soundscape_{:d}.txt".format(n))

        sc.generate(audiofile,
                    allow_repeated_label=True,
                    allow_repeated_source=False,
                    reverb=0.1,
                    disable_sox_warnings=True,
                    no_audio=False,
                    txt_path=None)




    for n in range(n_soundscapes_other):

        if (n%1000==0):
            print('Generating soundscape without gunshot: {:d}/{:d}'.format(n+1, n_soundscapes_other))

        # create a scaper
        sc = scaper.Scaper(duration, fg_folder, bg_folder)
        sc.protected_labels = []
        sc.ref_db = ref_db

        # add background
        sc.add_background(label=('choose', []), 
                          source_file=('choose', []), 
                          source_time=('const', 0))

        # add random number of foreground events
        #n_events = np.random.randint(min_events, max_events+1)
        #for _ in range(n_events):
        sc.add_event(label=('choose', ['clapping', 'door_slamming', 'fireworks', 'snapping']),  #'microphone_tap' 'glass_breaking'
                        source_file=('choose', []),
                        source_time=(source_time_dist, source_time), 
                        event_time=(event_time_dist, event_time), 
                        event_duration=(event_duration_dist, event_duration), 
                        snr=(snr_dist, snr_min, snr_max),
                        pitch_shift=(pitch_dist, pitch_min, pitch_max),
                        time_stretch=None)
        # generate
        audiofile = os.path.join(outfolder, "other.Soundscape_{:d}.wav".format(n))
        jamsfile = os.path.join(outfolder, "other.Soundscape_{:d}.jams".format(n))
        txtfile = os.path.join(outfolder, "other.Soundscape_{:d}.txt".format(n))

        sc.generate(audiofile,
                    allow_repeated_label=True,
                    allow_repeated_source=False,
                    reverb=0.1,
                    disable_sox_warnings=True,
                    no_audio=False,
                    txt_path=None)
    snr = snr-15
    
