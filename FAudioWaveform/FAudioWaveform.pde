import processing.sound.*;
int ec;
SoundFile sample;
Waveform waveform;
Amplitude rms;
float smoothingFactor = 0.25;
float sum;
int samples = 100;

int startTime=0;
final int duration=100;

public void setup() {
  size(800, 500);
  
  background(0);
 frameRate(10);
  
  String[] emotionclass1 = loadStrings("emotionclassmodel1.txt");
String[] emotionclass2 = loadStrings("emotionclassmodel2.txt");
String[] audioname=loadStrings("audiofilename.txt");
String audionamestr=audioname[0];
  String e1=emotionclass1[0];
  String e2=emotionclass2[0];
  //String e1="2";
 //String e2="2";
 // print(e1.charAt(1));
//print("\n"+e2.charAt(1));
  if(e1=="1" && e2=="1")
  ec=1; //exhilarated,happy//
  
  else if(e1=="1" && e2=="2")
  ec=4; //relaxed,serene, calm//
  else if(e1=="2" && e1=="1")
  ec=2; //anxious, terrified, disgusted// decide better colours
  else //e1==2,e2==2//
  ec=3; //sad, depressed, bored//
  
  print(ec);
  sample = new SoundFile(this, audionamestr);
  //sample = new SoundFile(this, "beat.aiff");
  sample.loop();

  waveform = new Waveform(this, samples);
  waveform.input(sample);
  
  rms = new Amplitude(this);
  rms.input(sample);
}

public void draw() {
  
  waveformColor();
   noStroke();
  strokeWeight(2);
  noFill();
if(ec==1){
    int selected = (int)random(0, 4);
    /*int choicesR[] = {238,204,153,102,51};
    int choicesG[] = {238,204,153,102,51};
    int choicesB[] = {238,204,153,102,51};
    */
    /*
    int choicesR[] = {254,247,250,203,233};
    int choicesG[] = {252,246,252,244,246};
    int choicesB[] = {232,178,209,240,249};
    */
    int choicesR[] = {255,0,0,255};
    int choicesG[] = {0,255,0,255};
    int choicesB[] = {0,0,255,0};
    
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
    /*int choicesR[] = {255,255,255};
    int choicesG[] = {255,0,0};
    int choicesB[] = {0,0,255};
    */
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
  waveform.analyze();
  drawWaveform();  
  amplitudeRMSColor();
  drawAmplitudeRMS();
   if(millis()-startTime>duration){
   background(0);
   }
   startTime=millis();
   
  }
  void keyPressed() {
  final int k = keyCode;
  looping ^= k == 'P';
  redraw = k == 'S';
}
