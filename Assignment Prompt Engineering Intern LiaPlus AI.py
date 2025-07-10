def nursing_admission_process():
    print("Namaste! Main aapko Nursing College ke admission process mein guide karne ke liye yahan hoon.")
    admission_interest = input("Kya aap B.Sc Nursing course mein admission lena chahenge? (Haan(yes)/Nahi(No)): ").strip().lower()

    if admission_interest in ["haan", "yes", "batao", "kya hai?"]:
        print("Bahut accha! Chaliye sabse pehle eligibility check karte hain.")
        biology_subject = input("Bataiye, kya aapne 12th class mein Biology subject padha tha? (Haan(yes)/Nahi(No)): ").strip().lower()

        if biology_subject in ["haan", "yes"]:
            print("Shandaar! Aap eligible hain. Chaliye ab aapko course ke baare mein details batata hoon.")
            program_details = input("Hamara B.Sc Nursing program ek full-time 4 saal ka course hai. Zyada jankari chahiye program ke baare mein? (Haan/No): ").strip().lower()

            if program_details in ["haan", "yes"]:
                print("Course ki total fees ₹70,000 hai, jo 3 aasaan installments mein pay ki ja sakti hai:")
                print("Tuition Fees: ₹60,000")
                print("Transportation Fees: ₹10,000")
                print("Total Annual Fee: ₹70,000")
                print("Installments: ₹30,000 (admission), ₹20,000 (after 1st sem), ₹20,000 (after 2nd sem)")
                hostel_info = input("Hostel aur training facilities ke baare mein jaan-na chahenge? (Haan(yes)/Nahi(No)): ").strip().lower()

                if hostel_info in ["haan", "yes"]:
                    print("Aamare Delhi campus par safe aur hygienic hostel facility available hai:")
                    print("• 24x7 security with CCTV")
                    print("• Clean mess")
                    print("• Common study halls")
                    print("• Boys & girls ke liye separate hostels with warden")
                    print("Hospital training bhi milegi jisme aap real patients ke saath kaam karenge.")
                    college_location = input("Kya aap location ya surrounding area ke baare mein aur jaanna chahenge? (Haan(yes)/Nahi(No)): ").strip().lower()

                    if college_location in ["haan", "yes"]:
                        print("Hamara Nursing College Delhi mein located hai – ek well-connected aur safe city jahan medical training ke ample opportunities hain.")
                        recognition_info = input("Kya aap recognition ke baare mein aur jaanna chahenge? (Haan(yes)/Nahi(No)): ").strip().lower()

                        if recognition_info in ["haan", "yes"]:
                            print("College ko Indian Nursing Council (INC), Delhi se recognition mila hua hai. Aapki degree nationally valid hogi.")
                            clinical_training = input("Kya aap clinical training locations ke baare mein aur jaanna chahenge?(Haan(yes)/Nahi(No)): ").strip().lower()

                            if clinical_training in ["haan", "yes"]:
                                print("Clinical training aapko reputed hospitals mein milegi, jaise:")
                                print("• Ranchi Neurosurgery & Allied Science Hospital (Jharkhand)")
                                print("• Regional Hospital (Chartha)")
                                print("• District Hospital (Backundpur)")
                                print("• Community Health Centers")
                                scholarship_info = input("Aapko scholarship options bhi milte hain, jaise: (Haan(yes)/Nahi(No)): ").strip().lower()

                                if scholarship_info in ["haan", "yes"]:
                                    print("Government Post-Matric Scholarship (₹18k–₹23k) – SC/ST/OBC ke liye")
                                    print("Labour Ministry Scholarship (₹40k–₹48k) – Agar aapke paas Labour Card hai")
                                    print("Merit-Based Scholarships bhi available hain")
                                    print("Is program mein total 60 seats available hain. Admissions limited hain, isliye jaldi apply karein.")
                                    eligibility_recap = input("Kya aap eligibility criteria recap chahenge?(Haan(yes)/Nahi(No)): ").strip().lower()

                                    if eligibility_recap in ["haan", "yes"]:
                                        print("Admission ke liye:")
                                        print("• 12th mein Biology")
                                        print("• PNT Exam pass")
                                        print("• Age: 17–35 years")
                                        help_with_form = input("Kya main aapko admission form bharne mein help kar sakta hoon? Ya koi aur information chahiye? (Haan(yes)/Nahi(No)): ").strip().lower()

                                        if help_with_form in ["haan", "yes"]:
                                            print("Accha! Aap [website link] par visit karein ya contact karein [helpline]. Main saari details bhej deta hoon.")
                                        else:
                                            print("Koi baat nahi! Agar kabhi help chahiye toh hum hamesha yahin hain. Best wishes for your future!")
                                    else:
                                        print("Thik hai! Aap kisi bhi samay mujhe firse pooch sakte hain.")
                                else:
                                    print("Thik hai! Aap kisi bhi samay mujhe firse pooch sakte hain.")
                            else:
                                print("Thik hai! Aap kisi bhi samay mujhe firse pooch sakte hain.")
                        else:
                            print("Thik hai! Aap kisi bhi samay mujhe firse pooch sakte hain.")
                    else:
                        print("Thik hai! Aap kisi bhi samay mujhe firse pooch sakte hain.")
                else:
                    print("Thik hai! Aap kisi bhi samay mujhe firse pooch sakte hain.")
            else:
                print("Thik hai! Aap kisi bhi samay mujhe firse pooch sakte hain.")
        else:
            print("Maaf kijiye, lekin B.Sc Nursing mein admission ke liye 12th mein Biology hona zaroori hai. Kya aap kisi aur course ke baare mein jaanna chahenge?")
    else:
        print("Koi baat nahi! Agar kabhi nursing education ke baare mein jaanna ho, to hum hamesha yahin hain. All the best!")

# Start the admission process
nursing_admission_process()
