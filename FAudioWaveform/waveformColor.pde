void waveformColor(){
  noStroke();
  strokeWeight(2);
  noFill();
if(ec==1){
    int selected = (int)random(0, 5);
    int choicesR[] = {254,247,250,203,233};
    int choicesG[] = {252,246,252,244,246};
    int choicesB[] = {232,178,209,240,249};
    fill(choicesR[selected],choicesG[selected],choicesB[selected]);
  }
  else if(ec==2)
  {
    int selected = (int)random(0, 5);
    int choicesR[] = {240,0,96,128,64};
    int choicesG[] = {20,204,96,128,64};
    int choicesB[] = {20,0,96,128,64};
    fill(choicesR[selected],choicesG[selected],choicesB[selected]);
  }
  else if(ec==3)
  {
    int selected = (int)random(0, 5);
    int choicesR[] = {153,51,153,0,192};
    int choicesG[] = {204,153,253,0,192};
    int choicesB[] = {255,255,255,153,192};
    
    fill(choicesR[selected],choicesG[selected],choicesB[selected]);
  }
  else
  {
    int selected = (int)random(0, 5);
    int choicesR[] = {243,234,225,211,123};
    int choicesG[] = {204,184,199,227,197};
    int choicesB[] = {145,117,165,226,193};
    fill(choicesR[selected],choicesG[selected],choicesB[selected]);
  }
}
