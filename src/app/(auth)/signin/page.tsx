import Image from "next/image";
import React from "react";

const SigninPage = () => {
  return (
    <main className="flex h-full min-w-full">
      <section className="flex h-full flex-1 shrink-0 items-center justify-center">
        로그인 화면
      </section>
      <section className="flex flex-1 shrink-0 items-center justify-center rounded-bl-[12.5rem] bg-[linear-gradient(135deg,_rgba(207,232,255,1)_0%,_rgba(255,255,255,1)_100%)]">
        <div className="flex flex-col items-center">
          <div className="relative mb-[32px] aspect-[276/65] w-[276px]">
            <Image src="/images/logo-compound-horizontal.png" alt="로고" fill />
          </div>
          <h2 className="text-3xl font-semibold text-primary">
            진료 데이터의 새로운 눈, AEYE
          </h2>
          <div className="relative mt-[68px] aspect-[693.78/553.75] w-[600.78px]">
            <Image src="/images/docs.png" alt="랜딩 이미지" fill />
          </div>
        </div>
      </section>
    </main>
  );
};

export default SigninPage;
