module IO_interface

#include "Solver.h"

       implicit none

       interface
             subroutine IO_display(u_res,v_res,w_res,p_res,T_res,p_counter,simtime,maxdiv,mindiv,umaxmin,vmaxmin)
             implicit none
             real, intent(in) :: u_res,v_res,p_res,simtime,T_res,maxdiv,mindiv,w_res
             integer, intent(in) :: p_counter
             real, intent(in), dimension(2) :: umaxmin,vmaxmin
             end subroutine IO_display
       end interface

       interface
             subroutine IO_display_v2(simTime,solnX,T_res)
             implicit none
             real, intent(in) :: simTime,solnX,T_res
             end subroutine IO_display_v2
       end interface


       interface
             subroutine IO_write(x,y,uu,vv,pp,tt,ww,rr,blk,blockOffset)
             implicit none
             real, dimension(Nxb+1,Nyb+1), intent(in) :: x,y,uu,vv,pp,tt,ww,rr
             integer, intent(in) :: blk,blockOffset
             end subroutine IO_write
       end interface
end module IO_interface
