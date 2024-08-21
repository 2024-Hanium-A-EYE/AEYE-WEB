'use client';
import { useState, useEffect } from 'react';
import React from 'react';
import { Report } from "@/types";
import { MultiStepLoader as Loader } from "@/components/ui/multi-step-loader";

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

const ClientSideUploadForm = () => {
    const [isLoading, setLoading] = useState(false);
    const [currentLoadingState, setCurrentLoadingState] = useState(0);
  
    useEffect(() => {
      let socket: WebSocket;
  
      if (isLoading) {
        socket = new WebSocket('ws://0.0.0.0:2000/logs'); // WebSocket 서버 URL
        socket.onmessage = (event) => {
          const logMessage = event.data;
  
          if (logMessage.includes('AI 서버에 연결중')) {
            setCurrentLoadingState(0);
          } else if (logMessage.includes('사진을 분석중')) {
            setCurrentLoadingState(1);
          } else if (logMessage.includes('사진을 토대로 진단')) {
            setCurrentLoadingState(2);
          } else if (logMessage.includes('거의 다 왔어요')) {
            setCurrentLoadingState(3);
          } else if (logMessage.includes('AI 진단이 완료되었어요')) {
            setCurrentLoadingState(4);
            setLoading(false); // 로딩 완료 후 종료
          }
        };
  
        socket.onerror = (error) => {
          console.error('WebSocket error:', error);
        };
      }
  
      return () => {
        if (socket) {
          socket.close();
        }
      };
    }, [isLoading]);
  
    const handleFileUpload = async (event: React.ChangeEvent<HTMLInputElement>) => {
      const file = event.target.files?.[0];
      if (file) {
        const formData = new FormData();
        formData.append('image', file);
  
        setLoading(true); // 로딩 상태 시작
  
        try {
          const response = await fetch('http://0.0.0.0:2000/api/', {
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
