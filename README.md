# Agnet_sound_event_detector
This repository has for objective to explore the posibilities of detecting **sudent sound events** in real time, in particular gunshots, using state of the art **sound processing** and **AI**

- **The Augmented dataset part is for Training networks for gunshot detection**
- **The GAN dataset is for training a Generative Adversarial Network to generate artificial new gunshot waveforms**

I took inspiration on 4 scientific articles to experiment, trying to reproduce the described results :

- https://eejournal.ktu.lt/index.php/elt/article/view/28877 : "Efficient Feature Set Developed for Acoustic Gunshot Detection in Open Space"
- "Audio-Based Event Detection at Different SNR Settings Using Two-Dimensional Spectrogram Magnitude Representations"
- https://www.researchgate.net/publication/228741330_Gunshot_detection_in_noisy_environments : "Gunshot detection in noisy environments"
- https://ieeexplore.ieee.org/document/9006456 : "Low Cost Gunshot Detection using Deep Learning on the Raspberry Pi"

Other ressources :

- https://github.com/kan-bayashi/ParallelWaveGAN : GAN Generator to create vocoder
- https://github.com/chrisdonahue/wavegan : GAN Generator to create more usefull audio clips
