'use client';
import { useState, useEffect } from 'react';
import React from 'react';
import { Report } from "@/types";
import { MultiStepLoader as Loader } from "@/components/ui/multi-step-loader";
import { useRouter } from 'next/navigation';  // useRouter는 클라이언트 사이드에서만 동작

const loadingStates = [
  { text: "AI 서버에 연결중이에요..." },
  { text: "사진을 분석중이에요..." },
  { text: "사진을 토대로 진단을 내리는 중이에요..." },
  { text: "거의 다 왔어요..!" },
  { text: "AI 진단이 완료되었어요!" },
];

function getRandomDiagnosis() {
  const diagnoses: Report[] = [
    { diagnosis: "Glaucoma", probability: "85%" },
    { diagnosis: "Diabetic Retinopathy", probability: "78%" },
    { diagnosis: "Retinal Detachment", probability: "92%" },
    { diagnosis: "Cataract", probability: "88%" },
    { diagnosis: "Conjunctivitis", probability: "70%" },
    { diagnosis: "Keratoconus", probability: "80%" },
    { diagnosis: "Dry Eye Syndrome", probability: "75%" },
    { diagnosis: "Uveitis", probability: "82%" },
    { diagnosis: "Optic Neuritis", probability: "65%" },
    { diagnosis: "Age-Related Macular Degeneration (AMD)", probability: "90%" },
    { diagnosis: "Central Serous Retinopathy", probability: "76%" },
    { diagnosis: "Myopia", probability: "60%" },
    { diagnosis: "Hyperopia", probability: "62%" },
    { diagnosis: "Astigmatism", probability: "74%" },
    { diagnosis: "Retinitis Pigmentosa", probability: "68%" },
  ];

  const randomIndex = Math.floor(Math.random() * diagnoses.length);
  return diagnoses[randomIndex];
}


const ClientSideUploadForm = ({ patientId }: { patientId: string }) => {
  const [isLoading, setLoading] = useState(false);
  const [currentLoadingState, setCurrentLoadingState] = useState(0);

  const router = useRouter();  // useRouter는 클라이언트 사이드에서만 사용됩니다.

  useEffect(() => {
    let timer: NodeJS.Timeout;

    if (isLoading) {
      setCurrentLoadingState(0);  // 초기화 필요
      timer = setInterval(() => {
        setCurrentLoadingState((prev) => {
          if (prev < loadingStates.length - 1) {
            return prev + 1;
          } else {
            clearInterval(timer);
            setLoading(false); // 로딩 완료 후 종료
            router.push(`/patients/${patientId}/analysis`);

            return prev;
          }
        });
      }, 1000); // 1초 간격으로 로딩 상태 업데이트
    }

    return () => {
      clearInterval(timer);
    };
  }, [isLoading, router, patientId]);

    const handleFileUpload = async (event: React.ChangeEvent<HTMLInputElement>) => {
      const file = event.target.files?.[0];
      if (file) {
        
        const jsonData = {
          whoami: 'NextJS',
          message: 'Request AEYE Inference',
          operation: 'Inference',
        };
        
        // FormData 대신, JSON 데이터를 직접 요청의 body에 추가
        const formData = new FormData();
        
        const fileInput = document.querySelector('input[type="file"]') as HTMLInputElement;

      if (fileInput && fileInput.files && fileInput.files.length > 0) {
        formData.append('file', fileInput.files[0]);  // 선택된 파일 추가
        } else {
        console.error('File input element not found or no files selected');
        }
        
        // JSON 데이터를 FormData에 추가 (key-value 방식)
        for (const [key, value] of Object.entries(jsonData)) {
          formData.append(key, value);
        }
        
        setLoading(true);  // 로딩 상태 시작

        try {
          const response = await fetch('http://0.0.0.0:2000/api/web-network-operator/', {
            method: 'POST',
            body: formData,
          });
  
          if (!response.ok) {
            console.error('서버 응답 오류:', response.statusText);
          }
        } catch (error) {
          console.error('이미지 업로드 오류:', error);
        }
      }
    };

  return (
    <>
    <div className="absolute right-10 top-1/2 transform -translate-y-1/2">
      <label
        htmlFor="imageUpload"
        className="cursor-pointer rounded bg-blue-500 px-4 py-2 text-white hover:bg-blue-600"
      >
        데이터 등록
      </label>
      <input
        id="imageUpload"
        type="file"
        accept="image/*"
        className="hidden"
        onChange={handleFileUpload}
      />
    </div>

    <Loader
          loadingStates={loadingStates}
          loading={isLoading}
          duration={1000}
        />
    </>
  );
};

export default ClientSideUploadForm;
