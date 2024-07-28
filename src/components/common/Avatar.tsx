"use client";

import { signout } from "@/actions/signout";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuShortcut,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import Image from "next/image";
import { useRouter } from "next/navigation";
import { FormEventHandler } from "react";

const Avatar = () => {
  const router = useRouter();
  const onSignOut: FormEventHandler<HTMLFormElement> = async (e) => {
    e.preventDefault();
    await signout();
    router.push("/");
  };

  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <div className="relative aspect-square w-[46px] cursor-pointer overflow-hidden rounded-full border">
          <Image
            src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?q=80&w=2564&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
            alt="아바타"
            className="object-cover"
            fill
          />
        </div>
      </DropdownMenuTrigger>
      <DropdownMenuContent className="w-48">
        <DropdownMenuLabel>내 계정: test@test.com</DropdownMenuLabel>
        <DropdownMenuSeparator />
        <DropdownMenuItem asChild>
          <form onSubmit={onSignOut} className="w-full">
            <button className="flex w-full justify-between">
              로그아웃
              <DropdownMenuShortcut>⇧⌘Q</DropdownMenuShortcut>
            </button>
          </form>
        </DropdownMenuItem>
      </DropdownMenuContent>
    </DropdownMenu>
  );
};

export default Avatar;
