import { Patient } from "@/types";
import { notFound } from "next/navigation";

export async function generateStaticParams() {
  const patients: Patient[] = await fetch(
    "http://localhost:3000/api/patients"
  ).then((res) => res.json());

  return patients.map((patient) => ({
    id: patient.id.toString(),
  }));
}

const fetchPatientById = async (id: string): Promise<Patient | null> => {
  const res = await fetch(`http://localhost:3000/api/patients/${id}`);
  if (!res.ok) {
    return null;
  }
  return res.json();
};

const PatientDetailPage = async ({ params }: { params: { id: string } }) => {
  const patient = await fetchPatientById(params.id);

  if (!patient) {
    notFound();
  }
  return (
    <main className="m-auto max-w-[1440px] px-8">
      <section>
        <h1>{patient.name}</h1>
        <p>Date of Birth: {patient.DOB}</p>
        <p>Symptom: {patient.symptom}</p>
        <p>Status: {patient.status}</p>
        {/* Add more details as needed */}
      </section>
    </main>
  );
};

export default PatientDetailPage;
