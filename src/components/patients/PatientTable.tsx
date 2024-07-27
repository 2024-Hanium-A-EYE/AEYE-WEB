"use client";

import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableFooter,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import Image from "next/image";
import { useRouter } from "next/navigation";

const patients = [
  {
    profileImage: "https://i.pravatar.cc/307",
    DOB: "2000.03.18 (만 24세)",
    numberOfVisits: 3,
    name: "김경서",
    symptom: "시야 어지러움, 시야각 좁아짐",
    recentVisitDate: "2024.07.20",
    severityPercentage: "80%",
    status: "HIGH_RISK",
  },
  {
    profileImage: "https://i.pravatar.cc/201",
    DOB: "1988.02.10 (만 36세)",
    numberOfVisits: 5,
    name: "이민지",
    symptom: "눈물 과다, 가려움",
    recentVisitDate: "2024.07.20",
    severityPercentage: "60%",
    status: "MODERATE_RISK",
  },
  {
    profileImage: "https://i.pravatar.cc/301",
    DOB: "1992.05.14 (만 32세)",
    numberOfVisits: 4,
    name: "최서연",
    symptom: "눈의 통증, 빛에 민감",
    recentVisitDate: "2024.07.15",
    severityPercentage: "40%",
    status: "NORMAL",
  },
  {
    profileImage: "https://i.pravatar.cc/302",
    DOB: "1975.08.24 (만 48세)",
    numberOfVisits: 9,
    name: "김영수",
    symptom: "시야 흐림, 눈의 피로",
    recentVisitDate: "2024.06.28",
    severityPercentage: "70%",
    status: "HIGH_RISK",
  },
  {
    profileImage: "https://i.pravatar.cc/280",
    DOB: "2002.10.09 (만 21세)",
    numberOfVisits: 2,
    name: "장민준",
    symptom: "눈의 건조함, 눈 깜박임 증가",
    recentVisitDate: "2024.07.05",
    severityPercentage: "25%",
    status: "LOW_RISK",
  },
  {
    profileImage: "https://i.pravatar.cc/400",
    DOB: "1985.12.30 (만 38세)",
    numberOfVisits: 6,
    name: "홍수민",
    symptom: "이중 시야, 눈부심",
    recentVisitDate: "2024.07.02",
    severityPercentage: "50%",
    status: "MODERATE_RISK",
  },
  {
    profileImage: "https://i.pravatar.cc/317",
    DOB: "1999.03.05 (만 25세)",
    numberOfVisits: 8,
    name: "서은우",
    symptom: "눈의 통증, 시력 감소",
    recentVisitDate: "2024.07.12",
    severityPercentage: "85%",
    status: "HIGH_RISK",
  },
];

const PatientTable = () => {
  const router = useRouter();
  return (
    <Table>
      <TableCaption>2024.06.01 ~ 2024.06.30 환자 리스트</TableCaption>
      <TableHeader>
        <TableRow>
          <TableHead className="w-[100px]"></TableHead>
          <TableHead className="text-left font-semibold">이름</TableHead>
          <TableHead className="text-center font-semibold">
            최근 진료 날짜
          </TableHead>
          <TableHead className="text-center font-semibold">
            치료 진척도
          </TableHead>
          <TableHead className="text-right font-semibold">위험군</TableHead>
        </TableRow>
      </TableHeader>
      <TableBody>
        {patients.map((patient, idx) => (
          <TableRow
            className="cursor-pointer"
            key={idx}
            onClick={() => {
              router.push("signin");
            }}
          >
            <TableCell className="font-medium">
              <div className="relative size-10 overflow-hidden rounded-full">
                <Image
                  src={patient.profileImage}
                  alt="환자 사진"
                  fill
                  className="object-cover"
                />
              </div>
            </TableCell>
            <TableCell>
              {patient.name}
              <p className="text-sm text-gray-400">{patient.DOB}</p>
              <p className="text-sm text-gray-400">{`${patient.numberOfVisits}번째 내원`}</p>
              <p className="text-sm text-gray-400">{patient.symptom}</p>
            </TableCell>
            <TableCell className="text-center">
              {patient.recentVisitDate}
            </TableCell>
            <TableCell className="text-center">
              {patient.severityPercentage}
            </TableCell>
            <TableCell className="text-right">{patient.status}</TableCell>
          </TableRow>
        ))}
      </TableBody>
      <TableFooter>
        <TableRow>
          <TableCell colSpan={4}>Total</TableCell>
          <TableCell className="text-right">{patients.length}</TableCell>
        </TableRow>
      </TableFooter>
    </Table>
  );
};

export default PatientTable;
