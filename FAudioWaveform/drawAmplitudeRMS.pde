void drawAmplitudeRMS(){
  sum += (rms.analyze() - sum) * smoothingFactor;
  float rms_scaled = sum * (height/4) * 5;
 for(int i=0;i<=360;i++){
   ellipse(width/2 + cos(i)*rms_scaled/2,height/2 + sin(i)*rms_scaled/2,2,2);
 } 
}
