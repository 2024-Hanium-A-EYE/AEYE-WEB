import { Patient } from "@/types";
import { notFound } from "next/navigation";
import Image from "next/image";
import CheckupList from "@/components/patients/CheckupList";
import { type Metadata } from "next";

import { promises as fs } from 'fs';
import { join } from 'path';
const jsonFilePath = join(process.cwd(), 'src', 'database', 'patients.json');

////////////////////////////////////////////////////////////////////////

const fetchPatientById = async (id: string): Promise<Patient | null> => {
  try {
    const patients = await getAllPatients();
    const patient = patients.find((patient) => patient.id.toString() === id);
    return patient || null;
  } catch (error) {
    console.error(`Failed to fetch patient with ID ${id}:`, error);
    return null;
  }
};

const getAllPatients = async (): Promise<Patient[]> => {
  try {
    const data = await fs.readFile(jsonFilePath, 'utf-8');
    return JSON.parse(data) as Patient[];
  } catch (error) {
    console.error('Failed to read patients JSON file:', error);
    throw new Error('Failed to load patient data');
  }
};

export async function generateStaticParams() {
  try {
    const patients = await getAllPatients();

    return patients.map((patient) => ({
      id: patient.id.toString(),
    }));
  } catch (error) {
    console.error("Error reading patients JSON:", error);
    return [];
  }
}



// Metadata를 동적으로 생성
export async function generateMetadata({
  params,
}: {
  params: { id: string };
}): Promise<Metadata> {
  const patient = await fetchPatientById(params.id);
  return {
    title: patient ? `${patient.name} - 대시보드` : "404",
    description: "진료 데이터의 새로운 눈, AEYE",
  };
}

const PatientDetailPage = async ({ params }: { params: { id: string } }) => {
  const patient = await fetchPatientById(params.id);

  if (!patient) {
    notFound();
  }
  return (
    <main className="m-auto max-w-[1440px] px-8 pb-10">
      <section>
        <h1 className="mb-12 text-3xl font-semibold">{`${patient.name} 님의 진료 기록`}</h1>
        <div className="flex h-40 w-full gap-10 rounded-xl border p-5">
          <div className="relative size-28 overflow-hidden rounded-full">
            <Image
              src={patient.profileImage}
              alt="환자 사진"
              fill
              className="object-cover"
            />
          </div>
          <div className="flex h-full flex-col justify-start gap-1">
            <h2 className="mt-2 text-xl font-semibold text-gray-600">
              {patient.name}
            </h2>
            <p className="text-gray-400">{patient.DOB}</p>
            <p className="text-gray-400">{`${patient.numberOfVisits}번째 내원`}</p>
          </div>
          <p className="ml-40 self-center text-right text-lg">
            {patient.status}
          </p>
        </div>
      </section>
      <div className="h-20" />
      <section>
        <h2 className="mb-8 text-xl">날짜별 진료기록</h2>
        <CheckupList checkups={patient.checkups} />
      </section>
    </main>
  );
};

export default PatientDetailPage;
