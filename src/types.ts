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
};
