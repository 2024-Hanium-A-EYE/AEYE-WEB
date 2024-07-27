import Image from "next/image";
import Link from "next/link";
import React from "react";

const Navbar = () => {
  return (
    <header className="m-auto w-full">
      <nav className="m-auto flex w-full max-w-[1440px] items-center justify-between px-8 py-5">
        <div className="relative aspect-[276/65] w-[100px] cursor-pointer">
          <Link href="/patients">
            <Image src="/images/logo-compound-horizontal.png" alt="로고" fill />
          </Link>
        </div>
        <div className="relative aspect-square w-[60px] overflow-hidden rounded-full border">
          <Image
            src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?q=80&w=2564&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
            alt="아바타"
            className="object-cover"
            fill
          />
        </div>
      </nav>
    </header>
  );
};

export default Navbar;
