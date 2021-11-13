int ARD1=A0;
int ARD2=A1;
int ARD3=A2;
int ARD4=A3;
int got_cell=0;

#define in1_1 5
#define in2_1 6

#define in1_2 7
#define in2_2 2

#define in1_3 3
#define in2_3 4


void setup() {
  // put your setup code here, to run once:
   pinMode(ARD1, INPUT); 
   pinMode(ARD2, INPUT); 
   pinMode(ARD3, INPUT); 

}

void loop() {
  // put your main code here, to run repeatedly:
  if(digitalRead(ARD1)+digitalRead(ARD2)+digitalRead(ARD3)+digitalRead(ARD4)>0 and got_cell=0){ //command recieved to get a specific cell

    got_cell=1

    
    
    int ARD1_ =digitalRead(ARD1);
    int ARD2_ =digitalRead(ARD2);
    int ARD3_ =digitalRead(ARD3);
    int ARD4_ =digitalRead(ARD4);
    delay(10000);
    int row =ARD_1*1+ARD_2*2+ARD3_*4+ARD4_*8;

    digitalWrite(in1_1,HIGH);
    digitalWrite(in2_1,LOW);
    delay(10000*row);
    digitalWrite(in1_1,LOW);
    
  
    delay(1000);
    digitalWrite(in1_2,HIGH);
    digitalWrite(in2_2,LOW);
    delay(10000);
    digitalWrite(in1_2,LOW);
    
    
    
    
    delay(40000);


    delay(1000);
    digitalWrite(in1_3,HIGH);
    digitalWrite(in2_3,LOW);
    delay(1000);
    digitalWrite(in1_3,LOW);

        delay(1000);
    digitalWrite(in1_2,LOW);
    digitalWrite(in2_2,HIGH);
    delay(10000);
    digitalWrite(in2_2,LOW);

    digitalWrite(in1_1,LOW);
    digitalWrite(in2_1,HIGH);
    delay(10000*row/);
    digitalWrite(in2_1,LOW);
    
    
    
    
  }

  if(digitalRead(ARD1)+digitalRead(ARD2)+digitalRead(ARD3)+digitalRead(ARD4)>0 and got_cell=1){ //command recieved to return the cell

    got_cell=0

    
    delay(1000);
    int ARD1_ =digitalRead(ARD1);
    int ARD2_ =digitalRead(ARD2);
    int ARD3_ =digitalRead(ARD3);
    int ARD4_ =digitalRead(ARD4);

    int row =ARD_1*1+ARD_2*2+ARD3_*4+ARD4_*8;

    delay(1000);
    digitalWrite(in1_2,HIGH);
    digitalWrite(in2_2,LOW);
    delay(10000);
    digitalWrite(in1_2,LOW);


    digitalWrite(in1_1,HIGH);
    digitalWrite(in2_1,LOW);
    delay(10000*row/);
    digitalWrite(in1_1,LOW);

    delay(1000);
    digitalWrite(in1_2,LOW);
    digitalWrite(in2_2,HIGH);
    delay(10000);
    digitalWrite(in2_2,LOW);
    
  
    
    delay(40000);
    
  
    delay(1000);
    digitalWrite(in1_3,LOW);
    digitalWrite(in2_3,HIGH);
    delay(1000);
    digitalWrite(in2_3,LOW);

    delay(1000);
    digitalWrite(in1_2,HIGH);
    digitalWrite(in2_2,LOW);
    delay(10000);
    digitalWrite(in1_2,LOW);

    digitalWrite(in1_1,LOW);
    digitalWrite(in2_1,HIGH);
    delay(10000*row/);
    digitalWrite(in2_1,LOW);
    
    
    
  }
  
}
