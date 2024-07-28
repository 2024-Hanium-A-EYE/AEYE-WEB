export type SigninSchema = {
  email: string;
  password: string;
};

export type Patient = {
  id: number;
  profileImage: string;
  DOB: string;
  numberOfVisits: number;
  name: string;
  symptom: string;
  recentVisitDate: string;
  severityPercentage: string;
  status: "HIGH_RISK" | "MODERATE_RISK" | "LOW_RISK" | "NORMAL";
  checkups: Checkup[];
};

export type Checkup = {
  checkupId: number;
  patientId: number;
  date: string;
  symptom: string;
  status: "HIGH_RISK" | "MODERATE_RISK" | "LOW_RISK" | "NORMAL";
  ultrasoundImages: string[];
  report: string;
};
