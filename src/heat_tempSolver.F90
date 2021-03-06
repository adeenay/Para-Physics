subroutine heat_tempSolver(tstep,T,T_old,mdot,smrh,u,v,a1x,a1y,a2x,a2y,s,pf,thco,cp)

#include "Solver.h"

      !$ use omp_lib
      use Grid_data
      use IncompNS_data
      use HeatAD_data
      use Driver_data
      use Multiphase_data, only: mph_cp2,mph_thco2,mph_max_s,mph_min_s
      use IBM_data, only: ibm_cp1,ibm_thco1

      implicit none
      
      integer, intent(in) :: tstep
      real, intent(inout), dimension(:,:) :: T,T_old,mdot,smrh,u,v,a1x,a1y,s,pf,thco,cp,a2x,a2y

      integer :: i,j,ii,jj

      real :: u_plus, u_mins, v_plus, v_mins, u_conv, v_conv
      real :: Tx_plus, Tx_mins, Ty_plus, Ty_mins
      real :: Tij, Tipj, Timj, Tijp, Tijm
      real :: Txx, Tyy, th, dxp, dxm, dyp, dym
      real :: alphax_plus, alphax_mins, alphay_plus, alphay_mins, alpha_interface
      real :: E_source

      real :: tol
      real :: Tsat

      tol = 0.01

      Tsat = 0.0

#ifdef TEMP_SOLVER_CENTRAL

   T(2:Nxb+1,2:Nyb+1) = T_old(2:Nxb+1,2:Nyb+1) &
  +((dr_dt*ins_inRe)/(ht_Pr*(gr_dx**2)))*(T_old(3:Nxb+2,2:Nyb+1)+T_old(1:Nxb,2:Nyb+1)-2*T_old(2:Nxb+1,2:Nyb+1))&
  +((dr_dt*ins_inRe)/(ht_Pr*(gr_dy**2)))*(T_old(2:Nxb+1,3:Nyb+2)+T_old(2:Nxb+1,1:Nyb)-2*T_old(2:Nxb+1,2:Nyb+1))&
  -((dr_dt*(u(2:Nxb+1,2:Nyb+1) + u(1:Nxb,2:Nyb+1))/2)/(gr_dx+gr_dx))&
   *(T_old(3:Nxb+2,2:Nyb+1)-T_old(1:Nxb,2:Nyb+1))&
  -((dr_dt*(v(2:Nxb+1,2:Nyb+1) + v(2:Nxb+1,1:Nyb))/2)/(gr_dy+gr_dx))&
  *(T_old(2:Nxb+1,3:Nyb+2)-T_old(2:Nxb+1,1:Nyb))

#endif

#ifdef TEMP_SOLVER_UPWIND

  !$OMP PARALLEL DEFAULT(NONE) PRIVATE(i,j,u_conv,v_conv,u_plus,u_mins,&
  !$OMP v_plus,v_mins,Tx_plus,Tx_mins,Ty_plus,Ty_mins,ii,jj) NUM_THREADS(NTHREADS) &
  !$OMP SHARED(T,T_old,dr_dt,gr_dy,gr_dx,ht_Pr,ins_inRe,u,v,dr_tile,a1x,a2x,a1y,a2y)

  !$OMP DO COLLAPSE(2) SCHEDULE(STATIC)

  !do jj=2,Nyb+1,dr_tile
  !do ii=2,Nxb+1,dr_tile
  !do j=jj,jj+dr_tile-1
     !do i=ii,ii+dr_tile-1
  do j=2,Nyb+1
     do i=2,Nxb+1

     u_conv = (u(i,j)+u(i-1,j))/2.
     v_conv = (v(i,j)+v(i,j-1))/2.

     u_plus = max(u_conv, 0.)
     u_mins = min(u_conv, 0.)

     v_plus = max(v_conv, 0.)
     v_mins = min(v_conv, 0.)

     Tx_plus = (T_old(i+1,j)-T_old(i,j))/gr_dx
     Tx_mins = (T_old(i,j)-T_old(i-1,j))/gr_dx

     Ty_plus = (T_old(i,j+1)-T_old(i,j))/gr_dy
     Ty_mins = (T_old(i,j)-T_old(i,j-1))/gr_dy

     T(i,j) = T_old(i,j)+((dr_dt*ins_inRe*0.5*(a2x(i,j)+a2x(i-1,j)))/(ht_Pr*gr_dx*gr_dx))*(T_old(i+1,j)+T_old(i-1,j)-2*T_old(i,j))&
                        +((dr_dt*ins_inRe*0.5*(a2y(i,j)+a2y(i,j-1)))/(ht_Pr*gr_dy*gr_dy))*(T_old(i,j+1)+T_old(i,j-1)-2*T_old(i,j))&
                        -((dr_dt))*(u_plus*Tx_mins + u_mins*Tx_plus)&
                        -((dr_dt))*(v_plus*Ty_mins + v_mins*Ty_plus)

     end do
  end do
  !end do
  !end do

  !$OMP END DO
  !$OMP END PARALLEL
#endif

end subroutine heat_tempSolver
