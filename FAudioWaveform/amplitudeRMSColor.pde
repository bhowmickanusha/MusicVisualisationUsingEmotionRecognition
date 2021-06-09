void amplitudeRMSColor(){
  noStroke();
  if(ec==1){
    int selected = (int)random(0, 6);
int choicesR[] = {238,204,153,102,51,0};
    int choicesG[] = {238,204,153,102,51,0};
    int choicesB[] = {238,204,153,102,51,0};
    fill(choicesR[selected],choicesG[selected],choicesB[selected]);
  }
  else
  {
    fill(0,0,120);
  }
}
