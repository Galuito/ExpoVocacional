int teamRed = 13;
int teamBlue = 12;

void setup() {
  // put your setup code here, to run once:
  pinMode(teamRed, OUTPUT);
  pinMode(teamBlue, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0){
    String msg = Serial.readString();
    
    if (msg == "red"){
      digitalWrite(teamRed, HIGH);
      digitalWrite(teamBlue, LOW);
    }
    else if(msg == "blue"){
      digitalWrite(teamBlue, HIGH);
      digitalWrite(teamRed, LOW);
    }
    else{
      digitalWrite(teamRed, HIGH);
      digitalWrite(teamBlue, HIGH);
    }
  }
}
