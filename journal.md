# static
i'm building this radio because i want an FM radio in my room that can also play audio if i want it to. since i have a HAM radio license, i gave this radio a sx1278 chip so it can listen to more bands that i can access.

my initial idea was to just follow the guide and add an audio jack as well as a rotary encoder, but i realized that was redundant. upon reworking my project, i made multiple more adjustments, adding a microSD card holder, an OLED display, an IR sensor, and the sx1278.

## 9/15 - [Schematic]

Today I worked on my schematic.
#### Hours Spent: 2
##### What did you do?:
Today, I used KiCAD to build the schematic for the radio. Finding the footprints took me a bit!

##### Why did you do it?:
I did this to create the schematic for my project, so it can be easily manufactured ofc!

##### What problems did you face?:
I faced issues with ERC (electric rules checker), mostly unused pins lol. Other than that, not much!
<img width="1112" height="510" alt="Screenshot 2026-09-18 at 11 35 54 PM" src="https://github.com/user-attachments/assets/bfe016e6-82b3-44ac-ac80-106b9d9864c3" />


## 9/16 - [PCB]
#### Hours Spent: 2
##### What did you do?:
Today, I used KiCAD to create the PCB for my project.

##### Why did you do it?:
This was done so that the radio can be manufactured!

##### What problems did you face?:
Not much, I accidentally used the wrong footprint for the XIAO at first but that was an easy fix :D

<img width="618" height="478" alt="Screenshot 2026-09-18 at 11 35 43 PM" src="https://github.com/user-attachments/assets/ce363fab-1f0f-43da-ac3c-fb7c039ee6e7" />
<img width="681" height="541" alt="Screenshot 2026-09-18 at 11 36 10 PM" src="https://github.com/user-attachments/assets/0fa06893-a03d-458d-9125-bc0941226034" />


## 9/20 - [reworking]
#### Hours Spent: 5
##### What did you do?:
Today, I used KiCAD to update the schematic and pcb for this project. I also wrote the firmware and updated my github directories and files to meet the criteria for submission.

##### Why did you do it?:
This was done to make a more effective radio that aligned with my goals better, as well as meeting the submission criteria for Static. I added multiple components: a microSD card holder, an OLED display, an IR sensor, and the sx1278, as well as things like crystals and mounting holes to make the overall project much better.

##### What problems did you face?:
I faced quite a few problems, first of all, i had trouble finding the footprint and symbol for the IR sensor i wanted, but i downloaded it from this website :https://app.ultralibrarian.com/details/625a961a-107f-11e9-ab3a-0a3560a4cccc/Vishay/TSOP38238?exports=42&open=exports, and was able to access it. I added it to my github as well. wiring also took much longer than last time due to the additional components, and passing the ERC and DRC was a struggle. Documenting everything also took quite a bit, with cart screenshots, a bom.csv, etc. etc.; but in the end, i'm incredibly proud of the progress i've made today and hope this can be accepted as a static submission. 
<img width="1211" height="606" alt="Screenshot 2026-09-20 at 2 40 43 PM" src="https://github.com/user-attachments/assets/d3bc4d65-dc44-4133-83f6-dce56819b65d" />
<img width="742" height="496" alt="Screenshot 2026-09-20 at 2 41 09 PM" src="https://github.com/user-attachments/assets/bb6c9575-4ae5-4b9f-9e93-6ba10da8e549" />
<img width="742" height="496" alt="Screenshot 2026-09-20 at 2 41 28 PM" src="https://github.com/user-attachments/assets/ba53e9df-230c-4e91-a51e-5ae14f48ed95" />
#### note
There was no CAD Case built for this project, so the case can be built later on once the antenna and potentiometer + button placement can be visualized. (I haven't decided on the button placement for this project yet, so I don't want to constrain placement just yet. Once it is assembled, a case will be built.)
