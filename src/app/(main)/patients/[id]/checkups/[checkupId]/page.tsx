import { Checkup, Patient } from "@/types";
import { notFound } from "next/navigation";
import React from "react";
import Image from "next/image";
import { Metadata } from "next/types";
import ImageUploader from "@/components/patients/ImageUploader";
import { Button } from "@/components/ui/button";

const fetchPatientById = async (id: string): Promise<Patient | null> => {
  const res = await fetch(`http://localhost:3000/api/patients/${id}`);
  if (!res.ok) {
    return null;
  }
  return res.json();
};

const fetchCheckupById = async (
  patientId: string,
  checkupId: string
): Promise<Checkup | null> => {
  const res = await fetch(
    `http://localhost:3000/api/patients/${patientId}/checkups/${checkupId}`
  );
  if (!res.ok) {
    return null;
  }
  return res.json();
};

// Metadata를 동적으로 생성
export async function generateMetadata({
  params,
}: {
  params: { id: string; checkupId: string };
}): Promise<Metadata> {
  const patient = await fetchPatientById(params.id);
  return {
    title: patient
      ? `${patient.name} - ${params.checkupId}번 진료 기록`
      : "404",
    description: "진료 데이터의 새로운 눈, AEYE",
  };
}

const CheckupDetailPage = async ({
  params,
}: {
  params: { id: string; checkupId: string };
}) => {
  const patient = await fetchPatientById(params.id);
  if (!patient) {
    notFound();
  }
  const checkup = await fetchCheckupById(params.id, params.checkupId);

  if (!checkup) {
    notFound();
  }

  return (
    <main className="m-auto max-w-[1440px] px-8 pb-10">
      <section>
        <h1 className="mb-12 text-3xl font-semibold">{`${patient.name} 님의 진료 기록 - ${checkup.date}`}</h1>
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
      <div className="h-10" />
      <div className="flex w-full gap-5">
        <ImageUploader initialSrc={checkup.ultrasoundImages[0]} />
        <ImageUploader initialSrc={checkup.ultrasoundImages[0]} />
      </div>
      <div className="h-10" />
      <Button>AI 진단 시작하기</Button>
      <div className="h-10" />
      <div className="rounded-lg border p-10">
        <h3 className="text-gray-600">
          {"AI Diagnosis: " + checkup?.report.ai.diagnosis}
        </h3>
        <p className="text-gray-600">
          {"Probability: " + checkup?.report.ai.probability}
        </p>
        <br />
        <h3 className="text-gray-600">
          {"Doctor's Diagnosis: " + checkup?.report.doctor.diagnosis}
        </h3>
      </div>
    </main>
  );
};

export default CheckupDetailPage;
