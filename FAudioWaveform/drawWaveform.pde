void drawWaveform(){
  beginShape();
  for(int i = 0; i < samples; i++){
    ellipse(
      map(i, 0, samples, 0, width),
      map(waveform.data[i], -0.5, 0.5, 0, height),
      3,3);
  }
  endShape();
}
